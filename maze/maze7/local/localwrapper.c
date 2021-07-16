#define _GNU_SOURCE
#include <string.h>
#include <unistd.h>

int main(void) {
	char *environment[1] = {0};
	char *argv[3] = {"./maze7", "public", 0};
	execve("./maze7", argv, environment);
}
