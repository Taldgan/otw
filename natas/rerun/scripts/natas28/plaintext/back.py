from urllib.parse import unquote
import base64
import sys
import subprocess
import requests
from requests.auth import HTTPBasicAuth

passw = subprocess.run(['getpass', '28'], stdout=subprocess.PIPE).stdout.decode('utf-8')
auth = HTTPBasicAuth('natas28', passw.strip())

def find_query(offset, character):
    payload = bytearray()
    payload_comp = bytearray()

    buff_comp = 'a'*10+'b'*16+'c'*3+'c'*offset
    buff = 'a'*10+'b'*48 #buffer, add line w/ 'padding' based off of length of 'character'


    payload_comp.extend(buff_comp.encode())
    payload.extend(buff.encode())
    padding = get_padding(character)
    payload.extend(padding)

    
    comp = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={b'query':bytes(payload_comp)}, allow_redirects=False)

    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={b'query':bytes(payload)}, allow_redirects=False)

    query = r.headers['Location']
    query_comp = comp.headers['Location']

    responses = [query_comp[18:], query[18:]]
    return responses


def get_padding(character):
    length = len(character)
    padding_len = 16-length
    padding = bytearray()
    for c in character:
        padding.append(c)
    for i in range(0, padding_len):
        padding.append(padding_len)
    return padding

def url_base64_to_hex(response):
    urldecoded = unquote(response[1])
    url_compdecoded = unquote(response[0])
    base64decoded = base64.b64decode(urldecoded)
    base64_compdecoded = base64.b64decode(url_compdecoded)
    hexed = base64decoded.hex()
    hexed_comp = base64_compdecoded.hex()
    hexedboth = [hexed, hexed_comp]
    return hexedboth

def split_newline(response):
    length = len(response[1])
    s = "" 
    for i in range(0,int(length/32)):
        if i == 6:
            s += response[1][32*i:32*i+32] + "\n" #line to solve
            
            s += response[0][32*i:32*i+32] + "\n" #comp line
    return s

def compare_lines(lines):
    comp_line = lines.split('\n')[0]
    test_line = lines.split('\n')[1]
    #print("Base: " + comp_line)
    #print("Test: " + test_line)

    if comp_line == test_line:
        return True
    return False

if __name__ == '__main__':
    plaintext = bytearray()
    for i in range(1, 16):
        count = 0
        for c in range(256):
            temp = bytearray()
            temp.append(c)
            temp.extend(plaintext)
            print(str(count) + ": Trying: " + str(bytes(temp)) + " | Offset = " + str(i))
            count += 1
            test = split_newline(url_base64_to_hex(find_query(i, temp)))
            print("Curr plaintext: " + str(plaintext))
            if compare_lines(test):
                found = bytearray()
                found.append(c)
                plaintext = found + plaintext 
                print("Found: " + str(chr(c)) + " | " + test + "\nPlaintext: " + str(plaintext))
                break
