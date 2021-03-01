global _start
_start:
	mov ebp, esp
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx
	push 0x79747469 ;itty
	push 0x4b6f6c6c ;lloK
	push 0x65486464 ;..He
	lea ecx, [esp+2]
	push eax 
	mov al, 4
	mov bl, 1
	mov dl, 12
	int 0x80
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx
	mov al, 1
	int 0x80
;nasm -f elf kitty.asm
;ld -m elf_i386 -s -o kitty kitty.o
;./kitty
