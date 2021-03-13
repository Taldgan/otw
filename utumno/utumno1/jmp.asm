global _start
_start:
	mov eax, 0xffffdfbf
	jmp eax
	
;nasm -f elf jmp.asm
;ld -m elf_i386 -s -o jmp jmp.o
;./jmp
