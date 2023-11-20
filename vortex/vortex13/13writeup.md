#vortex #pwn #otw #rop #ctf
# ToC
- [[##Level Summary]]
- [[##Level Description]]
- [[##Solution Details]]

# Vortex 13
## Level Summary
Malloc'd buf gets passed into `fgets`, then is used as the format for
`printf`, making it vulnerable to format string exploits.

## Level Description
This level seems to be a format string vulnerability level with extra steps.
`main` ensures no arguments could be passed in, and the environment/argv are cleared. 
It then calls `vuln`.

```c
int main(int argc, char **argv)
{
    int euid, i, j;
    // Exit if there are any arguments
    if (argc != 0) {
        exit(1);
    }
    // Clear environment
    for (i = 0; envp[i] != 0; i += 1) {
        for (j = 0; (envp[i][j]) != '\0'; j += 1) {
            (envp[i][j]) = 0;
        }
    }
    // Clear any straggling args
    for (i = 0; argv[i] != 0; i += 1) {
        for (j = 0; argv[i][j] != '\0'; j += 1) {
            argv[i][j] = 0;
        }
    }
    euid = geteuid();
    setreuid(euid, euid);
    // Call vulnerable function
    vuln();
    return 0;
}
```

The vulnerable function `vuln` then malloc's a buffer,
then fgets from stdin. It then compares all of the printf values against an
'allowed' list (ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%.$\n).
If any characters are placed in buf outside of that list, it breaks out of the loop.
Otherwise, after 20 characters (or a null), it calls printf on buf.
It then frees the buf, then returns.

```c
void vuln(void)
{
    char *buf;
    int succeeded, ind, i;
    char allowed[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789%.$\\n"

    buf = (char *) malloc(sizeof(char) * 20);
    succeeded = fgets(buf, 20, stdin);
    if (!succeeded) {
        exit(1);
    }
    i = 0;
    while( true ) {
        if (19 < i) {
            printf(buf);
            free(buf);
            return;
        }
        ind = strchr(_obj.allowed, buf[i]);
        if (ind == 0) {
            break;
        }
        i += 1;
    }
    exit(1);
}
```

## Solution Details

# Notes/Scratchpad
Maybe overwrite EBP of vuln in order to hijack return value of main?

Instead of a leave; ret, they reset esp based off of ecx? Kinda weird.
```
0x0804938e      call  sym.vuln      
0x08049393      mov   eax, 0
0x08049398      lea   esp, [var_10h]    ; Hijack value stored after the location of esp, we control ecx
0x0804939b      pop   ecx
0x0804939c      pop   ebx
0x0804939d      pop   ebp
0x0804939e      lea   esp, [ecx - 4]    ; Control ecx, we hijack esp - can set return addr?
0x080493a1      ret
```
Offset of 10 to access ebp on the stack
(0x%10$X prints ebp)

~Ok - what if I overwrite ebp, then use THAT stack address to get another write? :eyes:~

~Double stack write using `%f`?~ Can't get that to work either, even without positionals
```
1%f%f%f%f%x%n
1%f%f%f%f%x%n%16$x
1%f%f%f%f%x%n%18$x
1%f%f%f%f%x%n%1$x
```


## Potentially helpful webpages on more advanced format strings
### ["Advanced" Format String Exploitation](https://www.jaybosamiya.com/blog/2017/04/06/adv-format-string/)
Not too relevant to the level, except for the last paragraph.
What was interesting was the mention of a `__malloc_hook` - this function pointer is used whenever `malloc` is called.
If you overwrite it, and pass a width modifier larger than `64k` (`%70000c`, for example), `malloc` will get called, and thereby your hook.
Similar hooks exist for `free`, `realloc`, `memalign`, etc. Check with `man __malloc_hook`.
Could be helpful knowledge in the future.

The last (and potentially relevant to the level) section discusses format string write-what-wheres when the buffer we provide isn't 
on the stack. The description provided for that paragraph was unclear to me, but it did explain _not_ to use the position specifiers (i.e. `%10$x`).
That prevents us from overwriting a pointer on the stack, then using that pointer for the next format modifier because the position specifiers
actually make `printf` _copy_ the stack.

### [Format String exploits — when the buffer is not on the stack](https://anee.me/format-string-exploits-when-buffer-is-not-on-the-stack-f7c83e1a6781)
He uses positionals...?

### [Exploiting Format String Vulnerabilities](https://www.win.tue.nl/~aeb/linux/hh/formats-teso.html)
Discusses ways to walk more of the stack when length is limited
  - `%f`, `%.f` both consume 8 bytes at the cost of 2 or 3 bytes respectively (`%f` relies on having valid floating points on the stack, though)
      - Work to hit offset of `ebp`

Maybe find a way to overwrite `free` GOT entry with `system`?
