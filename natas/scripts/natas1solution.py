import re
import requests
from requests.auth import HTTPBasicAuth
import os
import natas0solution

auth = HTTPBasicAuth('natas1', natas0solution.get_pass())
def get_pass():
    r = requests.get('http://natas1.natas.labs.overthewire.org/', auth=auth)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
