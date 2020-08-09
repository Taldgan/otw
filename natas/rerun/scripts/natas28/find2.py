from urllib.parse import unquote
import base64
import sys
import subprocess
import requests
from requests.auth import HTTPBasicAuth

passw = subprocess.run(['getpass', '28'], stdout=subprocess.PIPE).stdout.decode('utf-8')
auth = HTTPBasicAuth('natas28', passw.strip())

def find_query():
    r = requests.post('http://natas28.natas.labs.overthewire.org/index.php/', auth=auth, data={'query':'a'*10+'b'*14+'%'+sys.argv[1]}, allow_redirects=False)
    query = r.headers['Location']
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
        if i == 3:
            s +=  response[32*i:32*i+12] + response[32*i+12:32*i+32]
    return s

if __name__ == '__main__':
    print(split_newline(url_base64_to_hex(find_query())))

