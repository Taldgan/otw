main:
- spawn 'safecode' thread
- set guid & uid to real uid/gid using SYSCALLS
- make call to 'unsafecode' (strcpy buf overflow)

- Since the syscall setresid & setresgid are used instead of the libc functions, only the main thread is impacted
- Safecode thread is a while loop that does printf("%d", 0)->fflush(stdout),sleep(1)
- From unsafecode we should somehow be able to impact & exploit privileged/elevated 'safecode' thread to spawn a shell
- Overwrite format string? GOT entry? idk


This was an interesting level! Last couple times I looked at it I didn't have an idea
for a solution - but this time I figured it out pretty quick.

This level has a relatively simple idea - it spawns a 'safe' thread
that has the setuid/elevated permissions of vortex9.

The 'safe' thread just runs a permanent while loop that
fflush's stdout and then calls printf("%d", 0);

It then makes syscalls to setgid & setuid to lower
the main thread privileges back to vortex8, then calls
the 'unsafe' function - which is just a strcpy

```c
  int main(int argc, char* argv[])
  {
      count = (undefined *)&param_1;
      // Spawn 'safe' thread
      pthread_create(&unused_var, 0, safecode, 0);
      our_gid = getgid();
      // Set gid to real gid (vortex 8)
      syscall(0xaa, our_gid, our_gid, our_gid);
      our_uid = getuid();
      // Set uid to real uid (vortex 8)
      syscall(0xa4, our_uid, our_uid, our_uid);
      // Call 'unsafe' code
      unsafecode(argv[1]);
      return 0;
  }
```

The 'safe' function

```c
  void safecode(void)
  {
      int32_t var_10h;
      
      do {
          printf(data.0804a008, 0);
          fflush(_stdout);
          sleep(1);
      } while( true );
  }
```

And finally the 'unsafe' function

```c
  void unsafecode(char *src)
  {
      char *dest;
      
      strcpy(&dest, src);
      return;
  }
```


Since the syscall was used to set the uid/gid, only the main thread has the lower permissions.
At the same time, the memory of the two threads are shared (with the exception of the heap).
With that in mind, we can exploit the 'unsafe' function and hijack the GOT in order to
overwrite a function pointer (fflush or printf) to call our shellcode from the elevated privilege
'safe' thread.

First we write the shellcode to overwrite the fflush function pointer:

```nasm
mov ebx, 0x0804c014  ; fflush GOT location in memory
mov dword ptr [ebx], 0xffffdfb4 ; overwrite fflush entry with shellcode addr
nop
jmp -1                ; jmp back for infinite loop          
```

This shellcode overwrites the GOT with the location of our shellcode to exec /bin/sh.
It also causes an infinite loop (nop->jmp -1) in order to keep the unprivileged thread
running while the safe thread executes /bin/sh, preventing an untimely crash.
* I think I left some extra bytes for that shellcode in the actual exploit,
  originally I was going to make a syscall to nanosleep 

Other than that, the shellcode mirrors the other levels - setuid/setgid to vortex9's id (5009)
and then execve /bin/sh!


* For some reason I could NOT for the life of me get the PoC to run on my local machine.
  It'd work in gdb, but the stack addresses did not match (not due to environment vars)
  when I'd analyze the coredump. Moved it over the the server and it executes fine. go figure