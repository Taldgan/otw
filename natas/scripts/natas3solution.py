import re
import requests
from requests.auth import HTTPBasicAuth
import natas2solution

auth = HTTPBasicAuth('natas3', natas2solution.get_pass())
def get_pass():
    r = requests.get('http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt', auth=auth)
    pass_regex = '[a-zA-Z0-9]'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
