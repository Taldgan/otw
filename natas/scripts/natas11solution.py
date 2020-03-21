import re
import requests
from requests.auth import HTTPBasicAuth
import subprocess

auth = HTTPBasicAuth('natas11', 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK')
def get_pass():
    cookie = {'data':subprocess.run(['php','natas11encrypt.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')}
    r = requests.get('http://natas11.natas.labs.overthewire.org/', auth=auth, cookies=cookie);
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
