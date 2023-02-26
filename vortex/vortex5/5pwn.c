#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>
#include <fcntl.h>

const unsigned short pLen = 5;
char *binPath = {"./vortex5alt"};

int makeAttempt(char *attempt);
int brute();

/** Function to initialize and adjust attempt string, then make that password attempt
 * to vortex5.
 * Returns the successful attempt, or NULL if no attempt was successful.
 **/
int brute(){
  char attempt[pLen+2];
  int i, focus = pLen -1, alphLen = 62;
  char alphabet[63] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
  '4', '5', '6', '7', '8', '9', '\0'};

  //Initialize attempt char array
  for(i = 0; i < pLen; i++){
    attempt[i] = 'a';
  }
  attempt[pLen] = '\n';
  attempt[pLen+1] = '\0';

  while(!makeAttempt(attempt)){
    //system("clear");
    usleep(50);
    printf("Attempt: %s", attempt);
    if(attempt[focus] == alphabet[alphLen-1]){
      attempt[focus] = alphabet[0];
      focus--;
      continue;
    }
    char* findChar = strchr(alphabet, attempt[focus]);
    int attemptIndex = (int)(findChar-alphabet);
    attempt[focus] = alphabet[attemptIndex+1];
    if(focus < pLen-1){
      focus++;
    }
  }
  printf("Successful attempt: %s", attempt);
  return 1;
}

/** Pass an attempt onto vortex5 binary and return true if password attempt was
    successful
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
  write(pipefd[1], attempt, 6);
  close(pipefd[1]);
  wait(0);
  char buf[200];
  char *childOut = buf+15;
  read(pipefd[0], buf, sizeof(buf));
  close(pipefd[0]);
  printf("Child output: %.19s\n", childOut);
  int x;
  if((x = strncmp("You got the right p", childOut, 19)) == 0)
    return 1;

  return 0;
}

int main(void) {
  brute();
  return 0;
}