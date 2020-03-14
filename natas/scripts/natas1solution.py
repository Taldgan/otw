import requests
from requests.auth import HTTPBasicAuth
import os
import natas0solution

auth = HTTPBasicAuth('natas1', natas0solution.get_pass())
def get_pass():
    r = requests.get('http://natas1.natas.labs.overthewire.org/', auth=auth)
    #print(r.url + "\n");
    webcontent = r.text
    #print(webcontent)
    i = webcontent.find('natas2 is')+10
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
