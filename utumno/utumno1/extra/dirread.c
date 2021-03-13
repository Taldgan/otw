#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>
#include <stdlib.h>


int main(int argc, char *argv[]){
	DIR *dir;
	struct dirent *rd;
	if(argc < 2){
		puts("Usage: ./test DIR");
		exit(1);
	}
	printf("Trying to open: %s\n", argv[1]);
	dir = opendir(argv[1]);
	if(dir == NULL){
		perror("ERROR: opendir returned NULL");
		exit(1);
	}
	printf("%s\n", argv[1]);
	printf("size rd: %lu\n", sizeof(*rd));
	while((rd = readdir(dir)) != NULL){
		printf("|__ %s\n", rd->d_name);
	}
	closedir(dir);
	return 0;
}
