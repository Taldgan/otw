import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    passw = subprocess.run(['getpass', '11'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas11', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    #Create cookie payload by running rewritten php file containing encrypted cookie with "showpassword"=>"yes"
    payload = {'data':subprocess.run(['php', 'xorencrypt.php'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()}
    #Pass cookie to website to get password
    r = requests.get('http://natas11.natas.labs.overthewire.org/', auth=('natas11', passw.strip()), cookies=payload)
    passreg = '[a-zA-Z0-9]{32}'
    #Print password using regex
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    get_pass()
