#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>
#include <fcntl.h>

const unsigned short pLen = 5;
char *binPath = {"./vortex5alt"};

/** Function to initialize and adjust attempt string, then make that password attempt
 * to vortex5.
 * Returns the successful attempt, or NULL if no attempt was successful.
 **/
int brute(){
  char attempt[6];
  int i;
  char alphabet[63] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
  '4', '5', '6', '7', '8', '9', '\0'};

  //Initialize attempt char array
  for(i = 0; i < pLen; i++){
    attempt[i] = 'a';
  }
  attempt[pLen] = '\0';

  return 1;
}

/** Pass an attempt onto vortex5 binary and log the output
 **/
int makeAttempt(char *attempt){
  int pipefd[2];

  //error if pipe() fails
  if(pipe(pipefd) == -1)
    return -1;
  //Child
  if(fork() == 0){
    char *args[2] = {binPath, NULL};
    //Copy file descriptor of STDOUT of child to pipefd stdout
    //While loop continues to run until dup2 is successful (and not failing)
    //just because of interrupts
    while((dup2(pipefd[1], STDOUT_FILENO) == -1) && errno != EINTR);
    while((dup2(pipefd[0], STDIN_FILENO) == -1) && errno != EINTR);
    write(pipefd[1], attempt, strlen(attempt));
    close(pipefd[1]);
    //replaces forked child process, but can still check pid of original
    //child to get exit code of vortex5
    execv(binPath, args);
  }
  printf("Attempt: %s", attempt);
  write(pipefd[1], attempt, 5);
  close(pipefd[1]);
  wait(0);
  char buf[200];
  char *childOut = buf+15;
  read(pipefd[0], buf, sizeof(buf));
  close(pipefd[0]);
  printf("Last letter: %c\n", buf[10]);
  printf("Child output: %s\n", childOut);
  int x;
  //Check for incorrect pass in output
  if((x = strncmp("Incorrect password\n", childOut, 19)) == 0)
    return 0;
  //If not, password found
  return 1;
}

int main(void) {
  //char password[pLen+1];
  //if((password = brute()) == NULL){
  //printf("No password found");
  //return 1;
  //}
  //printf("Password found: %s", brute());
  //if(makeAttempt("abcde\n")){
    //printf("pass found!\n");
  //}
  return 0;
}
