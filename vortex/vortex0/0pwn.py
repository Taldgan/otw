#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 0
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = 'vortex0'
PORT = 5842

def connect_to_level():
    #sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    #level 0 doesn't even ask for a username... or use ssh.
    #just sockets for this one
    r = remote(HOST, PORT)
    return r

def sum_bytes(r):
    summ = 0
    for i in range(0, 4):
        bytez = r.recvn(4, timeout=15)
        if not bytez:
            return 0
        summ += u32(bytez, sign='unsigned')
    return summ
summ = 4294967296
w = log.progress("Getting appropriate sum: ")
while summ > 4294967294:
    w.status("sum too high " + str(summ))
    r = connect_to_level()
    summ = sum_bytes(r)

w.success("Found appropriate sum '" + str(summ) + "'")
r.send(p32(summ))
r.recvuntil('Password: ' )
passw = r.recvall().decode('utf-8')
r.close()
time.sleep(1)
log.success('Vortex 1 password: ' + passw)


