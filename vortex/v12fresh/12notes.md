#pwn #otw #rop #ctf
# Vortex 12
## Level Summary
A call to `strcpy` in an unsafe thread leads to hijacked control flow.
A 'safe' thread that calls `printf` has elevated permissions - so
the idea is to overwrite the `printf` GOT entry and its argument
to gain a shell from the unsafe thread. 
NX is enabled, so a rop chain to mprotect is required.

## Level Description
Level is similar to vortex8 - except the stack is non-executable

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

The 'unsafe' code is just a strcpy on the provided src (argv[1] from the call in main).
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

To start - we've got to 
