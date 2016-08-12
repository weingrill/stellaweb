#!/usr/bin/python

import serial
import json
import requests

from datetime import datetime

from settings import API_URL, API_USER, API_PASS

#ser = serial.Serial('/dev/ttyr08', 57600, timeout=1)
ser = serial.Serial('/dev/ttyr0a', 115200, timeout=1)
# read analog channel one
cmd = "AD1R"
ser.write(chr(0x02)+"0"+cmd+chr(0x03))
ret=ser.read(size=255)
#print ret

ack = ret[1]
counts = int(ret[2:-1])
val = float(ret[2:-1])*5./1024.

if ack != chr(0x06):
  exit(1)

#print "A/D port 1: %f V" % val
# we measure half the voltage (0-5 instead of 0-10), so we multiply reading with 2
# Pfeiffer
#mbar = 10**((val*2.) * 1.667 - 11.33)
# Edwards
mbar = 10**((val*3.)-12.)
print "%e mbar" % (mbar)
