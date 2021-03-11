run: build
	/utumno/utumno0
	
build: hook.so

hook.so: hook.c
	gcc -m32 hook.c -o hook.so -fPIC -shared -ldl -D_GNU_SOURCE
clean:
	rm -rf *.so 2>/dev/null
	rm -rf *.o 2>/dev/null
	rm -f Lab1 2>/dev/null
