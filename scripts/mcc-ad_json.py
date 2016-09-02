#!/usr/bin/python

import serial
import json
import requests

verbose = False

from datetime import datetime

from settings import API_URL, API_USER, API_PASS

ser = serial.Serial('/dev/ttyr0a', 115200, timeout=1)
# read analog channel one
cmd = "AD1R"
ser.write(chr(0x02)+"0"+cmd+chr(0x03))
ret=ser.read(size=255)

ack = ret[1]
counts = int(ret[2:-1])
val = float(ret[2:-1])*5./1024.
if verbose: print "A/D reading: %s" % float(ret[2:-1])

if ack == chr(0x05):
  print "NAK"
else:
  print "Unknown response"

#print "A/D port 1: %f V" % val
# we measure half the voltage (0-5 instead of 0-10), so we multiply reading with 2
# Pfeiffer
#mbar = 10**((val*2.) * 1.667 - 11.33)
# Edwards
mbar = 10**((val*3.)-12.)
if verbose: print "A/D port 1: %f V %e mbar" % (val, mbar)

import subprocess

#root@ccd:~/src/sci-sta0500-wifsip# ./get_temp localhost
p = subprocess.Popen(['/usr/bin/ssh', 'root@ccd', 'src/sci-sta0500-wifsip/get_temp localhost'], stdout=subprocess.PIPE)
result, errorcode = p.communicate(input=None)
# returns
#result = 'temp0 = -119.756752 temp1 = -132.314744 temp2 = -118.464155 temp3 = -112.033779\n'
splitresult = result.rstrip('\n').split(' ')
temp0 = float(splitresult[2])
temp1 = float(splitresult[5])
temp2 = float(splitresult[8])
temp3 = float(splitresult[11])
if verbose: print temp0, temp1, temp2, temp3

# prepare JSON data block

timestamp = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')

data = json.loads(json.dumps({
    'datemeas': timestamp,
    'counts': counts,
    'volts': val,
    'mbar': '%e' % mbar,
    'temp0': temp0,
    'temp1': temp1,
    'temp2': temp2,
    'temp3': temp3
}))

request = requests.post(API_URL + 'ingest/', auth=(API_USER, API_PASS), json=data)

if request.status_code != 200:
    print request.text
