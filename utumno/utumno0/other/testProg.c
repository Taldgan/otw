#include <stdio.h>
int hookTargetFunction(){
	printf("%s", "Calling original function!\n");	
	return 5;
}

int main(){
	printf("The number is: %d\n", hookTargetFunction());
	return 0;
}
