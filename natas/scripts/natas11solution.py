import requests
from requests.auth import HTTPBasicAuth
import natas10solution
import subprocess

auth = HTTPBasicAuth('natas11', natas10solution.get_pass())
def get_pass():
    cookie = {'data':subprocess.run(['php','natas11encrypt.php'], stdout=subprocess.PIPE).stdout.decode('utf-8')}
    r = requests.get('http://natas11.natas.labs.overthewire.org/', auth=auth, cookies=cookie);
    webcontent = r.text
    #print(webcontent)
    i = webcontent.find('natas12 is')+11
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)

