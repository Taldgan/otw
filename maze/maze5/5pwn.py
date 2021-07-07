#!/usr/bin/python3
from pwn import *
import os
import time

#Level information for ssh
level = 5
USER = 'maze%s' % level
HOST = 'maze.labs.overthewire.org'
PASS = 'ishipaeroo'
PORT = 2225

#Variables for solving maze5 (username and pass)
username='maldgann'
passw='DP:EFB61'


def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT)
    return sh

def execute_maze(sh):
    time.sleep(0.03)
    w = log.progress("Executing maze 5...")
    shell = sh.run(b'/maze/maze5')
    time.sleep(0.03)
    shell.sendline(username)
    time.sleep(0.03)
    shell.sendline(passw)
    w.success("maze6 shell established")
    shell.interactive()

sh = connect_to_level()
execute_maze(sh)
