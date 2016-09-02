#!/usr/bin/python
import subprocess
from datetime import datetime
import json
import requests
from settings import API_PASS, API_URL, API_USER

#root@ccd:~/src/sci-sta0500-wifsip# ./get_temp localhost


result = subprocess.check_output(['/usr/bin/ssh', 'root@ccd', '/src/sci-sta0500-wifsip/get_temp localhost'])
# returns
result = 'temp0 = -119.756752 temp1 = -132.314744 temp2 = -118.464155 temp3 = -112.033779\n'
splitresult = result.rstrip('\n').split(' ')
temp0 = float(splitresult[2])
temp1 = float(splitresult[5])
temp2 = float(splitresult[8])
temp3 = float(splitresult[11])
print temp0, temp1, temp2, temp3

timestamp = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')

data = json.loads(json.dumps({
    'datemeas': timestamp,
    'temp0': temp0,
    'temp1': temp1,
    'temp2': temp2,
    'temp3': temp3
}))

request = requests.post(API_URL + 'ingest/', auth=(API_USER, API_PASS), json=data)

if request.status_code != 200:
    print request.text
