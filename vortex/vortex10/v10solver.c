#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <time.h>
#include <sys/times.h>
#include <unistd.h>

#define READ_BUF_SIZE 1000
#define NUM_BUF_SIZE 30
#define NUM_RAND_NUMS 20
#define READ_END 0
#define WRITE_END 1

int *parse_rand_nums(char* number_list);
uint gen_20_seed(int *our_num_list);

char *exec_read_out(char *prog) {
  int num_read = 0;
  char read_buf[READ_BUF_SIZE];
  char *ret_buf; 

  int dup_me_pipe[2];
  int read_pipe[2];

  if (pipe(dup_me_pipe) < -1) {
    fprintf(stderr, "Failed to create dup pipe\n");
    exit(EXIT_FAILURE);
  }

  if (pipe(read_pipe) < -1) {
    fprintf(stderr, "Failed to create read dup pipe\n");
    exit(EXIT_FAILURE);
  }

  int pid = fork();

  // Child
  if (pid == 0) {
    if(dup2(read_pipe[READ_END], STDIN_FILENO) < 0) {
      fprintf(stderr, "dup2 for child proc failed\n");
      exit(EXIT_FAILURE);
    }
    if(dup2(dup_me_pipe[WRITE_END], STDOUT_FILENO) < 0) {
      fprintf(stderr, "dup2 for child proc failed\n");
      exit(EXIT_FAILURE);
    }
    close(dup_me_pipe[READ_END]);
    close(dup_me_pipe[WRITE_END]);
    close(read_pipe[READ_END]);
    close(read_pipe[WRITE_END]);
    execl(prog, prog, NULL);
    fprintf(stderr, "Exec '%s' failed\n", prog);
    exit(EXIT_FAILURE);
  }

  // Parent
  close(dup_me_pipe[WRITE_END]);
  ret_buf = (char *) malloc(sizeof(char) * READ_BUF_SIZE);
  memset(ret_buf, 0, READ_BUF_SIZE);
  if (ret_buf == 0) {
    fprintf(stderr, "Failed to allocate ret buffer\n");
    exit(EXIT_FAILURE);
  }

  memset(read_buf, 0, READ_BUF_SIZE);
  while (1) {
    memset(read_buf, 0, READ_BUF_SIZE);
    if ((num_read = read(dup_me_pipe[READ_END], read_buf, READ_BUF_SIZE)) > 0) {
      printf("Read: (%d) %s\n", num_read, read_buf);
      strncat(ret_buf, read_buf, READ_BUF_SIZE-1);
      // Found ']' at end of list, stop reading output
      if (strrchr(ret_buf, ']') != NULL) {
        break;
      }
    }
    else {
      break;
    }
  }

  int * ret_list = parse_rand_nums(ret_buf);
  uint seed = gen_20_seed(ret_list);
  if (seed == 0) {
    fprintf(stderr,"No seed match found...\n");
    exit(EXIT_FAILURE);
  }
  free(ret_list);
  char cmd_to_send[] = "cat /etc/vortex_pass/vortex11\n";
  write(read_pipe[WRITE_END], &seed, 4);
  write(read_pipe[WRITE_END], cmd_to_send, sizeof(cmd_to_send));

  while (1) {
    memset(read_buf, 0, READ_BUF_SIZE);
    if ((num_read = read(dup_me_pipe[READ_END], read_buf, READ_BUF_SIZE)) > 0) {
      printf("Read: (%d) %s\n", num_read, read_buf);
      // Found ']' at end of list, stop reading output
    }
    else {
      break;
    }
  }

  // fprintf(stderr, "Complete Output: %s\n", ret_buf);
  return ret_buf;
}

int *parse_rand_nums(char* number_list) {
  int i, num_list_ind = 0, num_start, num_end;
  char num_buf[NUM_BUF_SIZE];
  int *ret_list = (int *) malloc(sizeof(int) * NUM_RAND_NUMS);

  if (number_list == NULL) {
    fprintf(stderr, "Null number list\n");
    exit(EXIT_FAILURE);
  }

  if (ret_list == 0){
    fprintf(stderr, "Failed to malloc number list\n");
    exit(EXIT_FAILURE);
  }
  num_list_ind += 2; // ignore '[ '
  for(i = 0; i < NUM_RAND_NUMS; i++) {
    memset(num_buf, 0, NUM_BUF_SIZE);
    num_start = num_list_ind;
    while(1) {
      char val = number_list[num_list_ind];
      if (val == '[' || val == ']') {
        num_list_ind ++;
        continue;
      }
      else if (val == '\0') {
        break;
      }
      else if (val == ',') {
        num_end = num_list_ind;
        num_list_ind++;
        break;
      }
      num_list_ind++;
    }  
    memcpy(num_buf, &number_list[num_start], num_end-num_start);
    sscanf(num_buf, "%08x", &ret_list[i]);
    printf("num %d: %08x\n", i + 1, ret_list[i]);
  }     

  return ret_list;
}

uint gen_20_seed(int *our_num_list) {
  clock_t clockVal;
  time_t time_now;
  int rand_int;
  uint user_input;
  int i, j;
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

  fprintf(stderr, "Seed (start): %08x\n", seed);
  for (j = 0; j < 500; j++) {
    //printf("\rj: %u\n", j);
    srand(seed-j);
    setvbuf(stdout,(char *)0x0,2,0);
    for (i = 0; i < calculated_seed_add_val; i = i + 1) {
      rand();
    }
    for (i = 0; i < 0x14; i = i + 1) {
      rand_int = rand();
      rand_values[i] = rand_int;
      if (rand_values[i] != our_num_list[i]) {
        break;
      }
      if (i == 19) {
        printf("\nFound seed match: %08x\n", seed-j);
        return seed-j;
      }
      //printf(" %08x,",rand_values[i]);
    }
  }
  printf("Seed (end): %08x\n", seed-j);
  return 0;
}

int main(int argc, char *argv[]) { 
  if (argc < 2) {
    fprintf(stderr, "Usage: %s <path to vortex10>\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  char * vortex_10_output = exec_read_out(argv[1]);

  // Parsed out list of integers, now need to identify seed
  return EXIT_SUCCESS;
}
