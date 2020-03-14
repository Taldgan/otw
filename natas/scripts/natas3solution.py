import requests
from requests.auth import HTTPBasicAuth
import natas2solution

auth = HTTPBasicAuth('natas3', natas2solution.get_pass())
def get_pass():
    r = requests.get('http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt', auth=auth)
    webcontent = r.text
#    print(webcontent)
    i = webcontent.find('natas4:')+7
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
