import re
import requests
from requests.auth import HTTPBasicAuth
import subprocess

auth = HTTPBasicAuth('natas8', 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe')
def get_pass():
    secret = subprocess.run(['php','natas8.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    dat = {'secret':secret, 'submit':'Submit'}
    r = requests.post('http://natas8.natas.labs.overthewire.org/', auth=auth, data=dat)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
