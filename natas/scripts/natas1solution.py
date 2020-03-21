import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas1', 'gtVrDuiDfck831PqWsLEZy5gyDz1clto')
def get_pass():
    r = requests.get('http://natas1.natas.labs.overthewire.org/', auth=auth)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
