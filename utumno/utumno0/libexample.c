#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>

int puts(const char *message){
	int (*new_puts)(const char *message);
	int result;
	new_puts = dlsym(RTLD_NEXT, "puts");
	result = new_puts("Dumping Contents!");	
	return result;
}
