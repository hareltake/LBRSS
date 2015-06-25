# -*- coding: utf-8 -*-
import sys
import re
from LBRSS_WS.tables import News, Position

Position.delete().execute()
f = open('position.txt', 'r')
for line in f:
	pos = line.split(', ')
	print pos[0]
	# Position.create(country=pos[0], city=pos[1])
	
f.close()
	