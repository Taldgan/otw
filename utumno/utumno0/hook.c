#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <dlfcn.h>

int puts(const char *message){
    int (*new_puts)(const char *message);
    int result;
    new_puts = dlsym(RTLD_NEXT, "puts"); //Assign funcP address to the real puts
    //printf("%x %x %x %x %x %x %x %x %x %x %x %x %x ", "ee"); //Print bytes in the stack, allows to find
	//addresses containing strings (0x80XXXXXX)
    int i;
    char* p = 0x8048489;  //After playing around with output, this address contains the starting point for 'password: '
    for(i = 0; i < 28; i++){
        putchar(*(p+i));		//Print 28 chars of the 'password: ' string using this address
    }
    result = new_puts("");
    return result;
}
