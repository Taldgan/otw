#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void print_hex(const char *s){
	printf(" 0x");
	while(*s){
		printf("%02x", (unsigned int) *s++);
	}
}

int main(int argc, char *argv[]){
	if(argc == 2){
		char *orig = malloc(strlen(argv[1])+1);
		strncpy(orig, argv[1], strlen(argv[1]));
		printf("Reversing \"%s\": %s\n", orig, memfrob(argv[1], strlen(argv[1])));
		printf("Hex: ");
		print_hex(orig);
		print_hex(argv[1]);
		puts("");
		free(orig);
		exit(0);
	}
	else{
		printf("Usage: %s memfrobstring\n", argv[0]);
	}
}
