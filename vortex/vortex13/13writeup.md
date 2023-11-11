#vortex #pwn #otw #rop #ctf
# ToC
- [[##Level Summary]]
- [[##Level Description]]
- [[##Solution Details]]

# Vortex 13
## Level Summary

## Level Description
Main of the level

```c
int main(int argc, char **argv)
{
    int euid;
    int i, j;

    if (argc != 0) {
        exit(1);
    }
    for (i = 0; envp[i] != 0; i += 1) {
        for (j = 0; (envp[i][j]) != '\0'; j += 1) {
            (envp[i][j]) = 0;
        }
    }
    for (i = 0; argv[i] != 0; i += 1) {
        for (j = 0; argv[i][j] != '\0'; j += 1) {
            argv[i][j] = 0;
        }
    }
    euid = geteuid();
    setreuid(euid, euid);
    vuln();
    return 0;
}
```

Vulnerable function `vuln`
```c
void vuln(void)
{
    char *buf;
    int succeeded;
    int ind;
    int i;
    size_t size;

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
