import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    auth = HTTPBasicAuth('natas0', 'natas0')
    r = requests.get('http://natas0.natas.labs.overthewire.org/', auth=auth);
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex, r.text)[0])

if __name__ == "__main__":
    get_pass()
