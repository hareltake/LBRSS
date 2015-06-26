# -*- coding: utf-8 -*-
import sys
import re
from LBRSS_WS.tables import News, Position
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

BASE_URL = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=true"
# Position.delete().execute()
f = open('position.txt', 'r')
for line in f:
    line = line.decode('utf-8')
    pos = line.split(',')
    pos[1] = pos[1][0:-1]
    if(pos[1] == ''):
        address = pos[0]
    else:
        address = pos[1]
    url = BASE_URL.format(address)
    s = requests.get(url)
    j = json.loads(s.text)
    print address
    lat = j['results'][0]['geometry']['location']['lat']
    lng =  j['results'][0]['geometry']['location']['lng']
    Position.create(country=pos[0], city=pos[1], lat=lat, lng=lng)


# for pos in Position.select().where(Position.country == '中国'):
#   print pos.city.__class__
#   