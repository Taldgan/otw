import requests
from requests.auth import HTTPBasicAuth
import natas1solution

auth = HTTPBasicAuth('natas2', natas1solution.get_pass())
def get_pass():
    r = requests.get('http://natas2.natas.labs.overthewire.org/files/users.txt', auth=auth)
    webcontent = r.text
#    print(webcontent)
    i = webcontent.find('natas3:')+7
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
