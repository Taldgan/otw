#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>


#define e(); printf("PTR: %u\nHEX: 0x%08x\n", (unsigned int)ptr,(unsigned int)ptr);if(((unsigned int)ptr & 0xff000000)==0xca000000) { setresuid(geteuid(), geteuid(), geteuid()); execlp("/bin/sh", "sh", "-i", NULL); }
void print(unsigned char *buf, int len, unsigned char *ptr)
{
        int i;
        printf("[ ");
        for(i=0; i < len; i++) 
			printf("%x ", buf[i]); 
        printf(" ]\n");
		printf("PTR: %u\nHEX: 0x%08x\n", (unsigned int)ptr,(unsigned int)ptr);
}

int main()
{
        unsigned char buf[512];
        unsigned char *ptr = buf + (sizeof(buf)/2);
        unsigned int x;

        while((x = getchar()) != EOF) {
                switch(x) {
                        case '\n': 
							print(buf, sizeof(buf), ptr); 
							continue; 
							break;
                        case '\\': 
							ptr--; 
							break; 
                        default: 
							e(); 
							if(ptr > buf + sizeof(buf)) 
								continue; 
							ptr++[0] = x; 
							break;
                }
        }
        printf("All done\n");
}
