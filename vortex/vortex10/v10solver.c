#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

#define READ_BUF_SIZE 1000
#define NUM_BUF_SIZE 30
#define NUM_RAND_NUMS 20
#define READ_END 0
#define WRITE_END 1

char *exec_read_out(char *prog) {
  int num_read = 0;
  char read_buf[READ_BUF_SIZE];
  char *ret_buf; 

  int dup_me_pipe[2];
  if (pipe(dup_me_pipe) < -1) {
    fprintf(stderr, "Failed to create dup pipe\n");
    exit(EXIT_FAILURE);
  }

  int pid = fork();

  // Child
  if (pid == 0) {
    if(dup2(dup_me_pipe[WRITE_END], STDOUT_FILENO) < 0) {
      fprintf(stderr, "dup2 for child proc failed\n");
      exit(EXIT_FAILURE);
    }
    close(dup_me_pipe[READ_END]);
    close(dup_me_pipe[WRITE_END]);
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

int main(int argc, char *argv[]) { 
  if (argc < 2) {
    fprintf(stderr, "Usage: %s <path to vortex10>\n", argv[0]);
    exit(EXIT_FAILURE);
  }
  char * vortex_10_output = exec_read_out(argv[1]);
  int * ret_list = parse_rand_nums(vortex_10_output);
  free(vortex_10_output);

  // Parsed out list of integers, now need to identify seed
  return EXIT_SUCCESS;
}
