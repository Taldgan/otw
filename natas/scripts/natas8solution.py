import requests
from requests.auth import HTTPBasicAuth
import natas7solution
import subprocess

auth = HTTPBasicAuth('natas8', natas7solution.get_pass())
def get_pass():
    secret = subprocess.run(['php','natas8.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    #secret = str(sys.argv[1])
    dat = {'secret':secret, 'submit':'Submit'}
    r = requests.post('http://natas8.natas.labs.overthewire.org/', auth=auth, data=dat)
    webcontent = r.text
#    print(webcontent)
#    print(secret)
    i = webcontent.find('natas9 is') + 10
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)
