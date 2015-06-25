# -*- coding: utf-8 -*-
import sys
import re
from LBRSS_WS.tables import News, Position

Position.delete().execute()
f = open('position.txt', 'r')
for line in f:
	line = line.decode('utf-8')
	pos = line.split(', ')
	Position.create(country=pos[0], city=pos[1])


for pos in Position.select().where(Position.country == '中国'):
	print pos.city.__class__
	