#!/usr/bin/python3
from pwn import *
import os
import time
import sys
import string

#MD5 Brute Force
#
#A password is required for the next level. vortex5.c and md5.h. a-z,A-Z,0-9 is the search space.
#The password length is 5 chars long, it was originally 7 chars long.
#
#Collision(s) tested : 489265082 in 217 second(s), 361 millisec, 101 microsec.
#Average of 2250932.1 hashes/sec

#Level information for ssh
level = 5
USER = 'vortex%s' % level
HOST = 'vortex.labs.overthewire.org'
PASS = 'Aap2dupto'
PORT = 2228

context.log_level = 'error'

def connect_to_level():
    sh = ssh(user=USER, host=HOST, password=PASS, port=PORT, timeout=60)
    return sh

def execute_payload(sh):
    time.sleep(0.05)
    w = log.progress("Executing vortex5")
    shell = sh.run('/vortex/vortex5')
    passw = b'rlTf6'
    shell.sendline(passw)
    w.success("Complete")
    log.success("vortex6 shell established")
    shell.interactive()

# A-Z    a-z      0-9
#65-90, 97-127,  48-57
def brute(binary, pass_len):
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    alph_len = 62
    attempt = ['r', 'l', 'T', 'a', 'a']
    #for i in range(0, pass_len):
        #attempt.append(alphabet[0])

    response = make_attempt(binary, attempt)
    w = log.progress("Attempt")

    focus = pass_len-1
    start = time.time()
    while 'Incorrect' in response:
        response = make_attempt(binary, attempt)
        if 'right password' in response:
            break
        if attempt[focus] == alphabet[alph_len-1]:
            log_attempt(attempt, w, start)
            attempt[focus] = alphabet[0]
            focus -= 1
            continue
        attempt[focus] = alphabet[alphabet.index(attempt[focus])+1]
        if focus < pass_len-1:
            focus += 1
        log_attempt(attempt, w, start)
    return attempt

def log_attempt(attempt, w, start):
    context.log_level = 'info'
    w.status(str(attempt) + " Incorrect\nTime Elapsed: " + str(int(time.time()-start)))
    context.log_level = 'error'

def make_attempt(binary, attempt_list):
    attempt = ''
    attempt = attempt.join(attempt_list)
    #time.sleep(0.01)
    p = binary.process(["./vortex5"], stdin=PTY)
    p.sendline(attempt.encode('utf-8'))
    p.recvline(timeout=1)
    if p.recvline(timeout=1) == b'':
        response = 'Incorrect'
    else:
        response = p.recvline(timeout=1).decode('utf-8')
    #print(response)
    p.close()
    return response

def local_payload():
    binary=ELF("vortex5")
    w = log.progress("Executing vortex 5")
    passw = ''
    print('Password is: '+ passw.join(brute(binary, 5)))


if len(sys.argv) == 2 and sys.argv[1] == "local":
    local_payload()

else:
    sh = connect_to_level()
    execute_payload(sh)
