/*
This tool was developed through the awesome community effort on reverseengineering.stackexchange.com

The Thread: http://reverseengineering.stackexchange.com/questions/98/how-can-i-analyse-an-executable-with-no-read-permission

Special thanks to:
 + igor-skochinsky who pointed at this Phrack article and gave the initial idea: http://www.phrack.com/issues.html?issue=63&id=12&mode=txt
 + gilles for his engagement and enthisiasm about this question and his code attempt
 + and all others who were involved

This new stackexchange reverseengineering community is FUCKING AWESOME!!! <3

*/
#include <stdio.h>
#include <sys/ptrace.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/user.h>
#include <sys/syscall.h>

int main()
{
    pid_t pid;

    pid = fork();
    if(pid == 0) {
        ptrace(PTRACE_TRACEME, 0, NULL, NULL);
        execl("/utumno/utumno0", "/utumno/utumno0", NULL);
    }
    else {
        int status;
        struct user_regs_struct regs;

        // single stepping until it reached the real code segment
        while(1) {

            wait(&status);
            if(WIFEXITED(status))
                break;

            // get registers for the instruction pointer
            ptrace(PTRACE_GETREGS, pid, NULL, &regs);

            // strace ./bin
            // brk(0) = 0x804a000
            if(regs.eip>0x804a000)
            {
                printf("in code section at EIP=%lx\n",regs.eip);
                unsigned int i;

                // Dump code
                for(i=0; i<0x1000; i+=4) {
                    long data = ptrace(PTRACE_PEEKTEXT, pid, regs.eip+i, 0);
                    printf("%lx",data);
                }
            }

            // single step in child process
            ptrace(PTRACE_SINGLESTEP, pid, NULL, NULL);
        }
    }
    return 0;
}
