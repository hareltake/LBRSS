# -*- coding: utf8 –*-
from tables import News, Position
for city in Position.select().where(Position.country == '中国'):
	print city.id
	# print city.news[0].title