#!/usr/bin/python
'''
Created on Aug 11, 2016

@author: Joerg Weingrill <jweingrill@aip.de>
'''

import json
import requests

from datetime import datetime

from settings import API_URL, API_USER, API_PASS


timestamp = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
counts = 479
val = 2.338867
mbar = 1.038967e-05

data = json.loads(json.dumps({
    'datemeas': timestamp,
    'counts': counts,
    'volts': val,
    'mbar': mbar
}))

request = requests.post(API_URL + 'ingest/', auth=(API_USER, API_PASS), json=data)

if request.status_code != 200:
    print request.text

print request.text
