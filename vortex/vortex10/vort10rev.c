#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/times.h>
#include <unistd.h>

int main(int argc,char **argv)
{
  clock_t clockVal;
  time_t time_now;
  int rand_int;
  __uid_t __suid;
  __uid_t __euid;
  __uid_t __ruid;
  int in_GS_OFFSET;
  uint user_input;
  int i;
  int calculated_seed_add_val;
  uint seed;
  struct tms tms_buf;
  int rand_values [20];
  int stack_cookie;
  
  clockVal = times(&tms_buf);
  calculated_seed_add_val =
         clockVal + tms_buf.tms_cstime + tms_buf.tms_utime + tms_buf.tms_stime + tms_buf.tms_cutime;
  clockVal = clock();
  calculated_seed_add_val = calculated_seed_add_val + clockVal;
  time_now = time((time_t *)0x0);
  calculated_seed_add_val = 0x80 - (calculated_seed_add_val + time_now) % 0x100;
  time_now = time((time_t *)0x0);
  seed = time_now + calculated_seed_add_val;
  srand(seed);
  setvbuf(stdout,(char *)0x0,2,0);
  for (i = 0; i < calculated_seed_add_val; i = i + 1) {
     rand();
  }
  putchar(L'[');
  for (i = 0; i < 0x14; i = i + 1) {
     rand_int = rand();
     rand_values[i] = rand_int;
     printf(" %08x,",rand_values[i]);
  }
  puts("]");
  alarm(30);
  read(0,&user_input,4);
  if (seed == user_input) {
     __suid = geteuid();
     __euid = geteuid();
     __ruid = geteuid();
     execlp("/bin/sh","sh",NULL,0);
  }
  else {
     puts("Nope, try again");
  }
  return 0;
}
