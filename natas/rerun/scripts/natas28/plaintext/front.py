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
    blah = 'a'*10+'b'*offset
    payload.extend(blah.encode())
    comp = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={b'query':bytes(payload)}, allow_redirects=False)
    payload.extend(character)
    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={b'query':bytes(payload)}, allow_redirects=False)
    query = r.headers['Location']
    query_comp = comp.headers['Location']
    responses = [query_comp[18:], query[18:]]
    return responses

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
        if(i == 3):
            s += response[1][32*i:32*i+32] + "\n"
            s += response[0][32*i:32*i+32] + "\n"
    return s

def compare_lines(lines):
    comp_line = lines.split('\n')[0]
    test_line = lines.split('\n')[1]
    if comp_line == test_line:
        return True
    return False

if __name__ == '__main__':
    plaintext = bytearray()
    for i in range(1, 16):
        count = 0
        for c in range(256):
            temp = bytearray()
            temp.extend(plaintext)
            temp.append(c)
            print(str(count) + ": Trying: " + str(bytes(temp)) + " | Offset = " + str(16-i))
            count += 1
            test = split_newline(url_base64_to_hex(find_query(16-i, temp)))
            if compare_lines(test):
                plaintext.append(c)
                print("Character: " + str(chr(c)) + " | " + test + "\nPlaintext: " + str(plaintext))
                break
