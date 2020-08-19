from urllib.parse import unquote
import base64
import sys
import subprocess
import requests
from requests.auth import HTTPBasicAuth

passw = subprocess.run(['getpass', '28'], stdout=subprocess.PIPE).stdout.decode('utf-8')
auth = HTTPBasicAuth('natas28', passw.strip())

def find_query():
    payload = bytearray()
    ppart = 'a'*10
    #print(ppart)
    payload.extend(ppart.encode())
    charr = get_padding(bytes(sys.argv[1].encode()))
    payload.extend(charr)
    print(payload)
    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={b'query':bytes(payload)}, allow_redirects=False)
    query = r.headers['Location']
    return query[18:]

def url_base64_to_hex(response):
    urldecoded = unquote(response)
    base64decoded = base64.b64decode(urldecoded)
    hexed = base64decoded.hex()
    return hexed

def get_padding(character):
    length = len(character)
    padding_len = 16-length%16
    padding = bytearray()
    for c in character:
        padding.append(c)
    for i in range(0, padding_len):
        padding.append(padding_len)
    return padding

def split_newline(response):
    length = len(response)
    print(length)
    s = ""
    if len(sys.argv) > 2 and sys.argv[2] == 'yes':
        for i in range(0,int(length/32)):
            s += str(i) + ": " + response[32*i:32*i+32] + "\n"
    else:
        for i in range(0, int(length/32)):
            if i > 2 and i < int(length/32)-2:
                s += response[32*i:32*i+32]
    return s

if __name__ == '__main__':
    print(split_newline(url_base64_to_hex(find_query())))

