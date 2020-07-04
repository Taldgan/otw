import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #"secret" value to beat level
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '8'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    secret = subprocess.run(['php', 'natas8/decode.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas8', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #Need to pass /etc/natas_webpass/natas8/ to view the natas8 password
    payload = {'secret':secret, 'submit':'Submit'}
    r = requests.post('http://natas8.natas.labs.overthewire.org/', auth=('natas8', passw.strip()), data=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
