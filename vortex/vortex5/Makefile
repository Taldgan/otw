run: build
	./5pwn

build: 5pwn.o vortex5alt.o
	gcc -ggdb 5pwn.o -o 5pwn
	gcc -ggdb vortex5alt.o -o vortex5alt

5pwn.o: 5pwn.c
	gcc -ggdb -c 5pwn.c

vortex5alt.o: vortex5alt.c
	gcc -ggdb -c vortex5alt.c

clean:
	rm -rf *.o 2>/dev/null
	rm -f 5pwn 2>/dev/null
	rm -f vortex5alt 2>/dev/null
