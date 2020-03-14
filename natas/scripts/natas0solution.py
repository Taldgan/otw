import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('natas0', 'natas0')
def get_pass():
    r = requests.get('http://natas0.natas.labs.overthewire.org/', auth=auth);
    #print(r.url + "\n");
    #print(r.text);
    webcontent = r.text
    i = webcontent.find('natas1 i')+10
    s = webcontent[i:i+32]
    return s
if __name__ == "__main__":
    solution = get_pass()
    print(solution)

