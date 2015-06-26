# -*- coding: utf8 –*-
from LBRSS_WS import app
from flask import render_template, flash, request, g, session, redirect, url_for, jsonify
from crawl import crawl
from tables import News, Position
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/map', methods=['GET'])
def map():
	all_news = []
	for pos in Position.select().where(Position.city == '黑龙江'):
		for news in pos.news:
			all_news.append([pos.lat, pos.lng, news.title, news.link, news.desc.strip()])
	return render_template('map.html', all_news=all_news)

@app.route('/allNews', methods=['GET'])
def getAllNews():
	all_news = []
	for pos in Position.select().where(Position.country == '中国'):
		for news in pos.news:
			all_news.append({'lat': pos.lat, 'lng': pos.lng, 'title': news.title.encode('utf-8'), 'link': news.link, 'desc': news.desc.encode('utf-8')})
	return jsonify({'news': all_news})
