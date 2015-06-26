# -*- coding: utf8 –*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tables import News, Position
for pos in Position.select().where(Position.country == '中国'):
	print pos.news.count()
	# print city.news[0].title