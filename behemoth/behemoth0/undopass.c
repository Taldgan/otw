#define _GNU_SOURCE
#include <string.h>
#include <stdio.h>

int main(void){
	char encrypted[11] = "OK^GSYBEX^Y";
	printf("Pass: %s\n", memfrob(encrypted, 11));
}
