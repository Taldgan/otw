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
    charr = bytes(bytearray.fromhex(sys.argv[1]))
    payload.extend(charr)
    print(payload)
    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={b'query':bytes(payload)}, allow_redirects=False)
    query = r.headers['Location']
    if len(sys.argv) > 2 and sys.argv[2] == 'yes':
        print(r.text)
    return query[18:]

def url_base64_to_hex(response):
    urldecoded = unquote(response)
    base64decoded = base64.b64decode(urldecoded)
    hexed = base64decoded.hex()
    return hexed
def split_newline(response):
    length = len(response)
    s = ""
    for i in range(0,int(length/32)):
        s += str(i) + ": " + response[32*i:32*i+32] + "\n"
    return s

if __name__ == '__main__':
    print(split_newline(url_base64_to_hex(find_query())))

