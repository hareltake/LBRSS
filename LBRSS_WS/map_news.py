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
	return render_template('map.html')

@app.route('/allNews', methods=['GET'])
def getAllNews():
	all_news = []
	for pos in Position.select():
		if pos.news.count() != 0:
			news = pos.news[0];
			all_news.append({'lat': pos.lat, 'lng': pos.lng, 'title': news.title.encode('utf-8'), 'link': news.link, 'desc': news.desc.encode('utf-8')})
	# print all_news
	return jsonify({'news': all_news})

@app.route('/newsByCountry', methods=['POST'])
def getNewsByCounty():
	country = request.form['country']
	all_news = []
	for pos in Position.select().where(Position.country == country):
		if pos.news.count() != 0:
			news = pos.news[0];
			all_news.append({'lat': pos.lat, 'lng': pos.lng, 'title': news.title.encode('utf-8'), 'link': news.link, 'desc': news.desc.encode('utf-8')})
	print len(all_news)
	return jsonify({'news': all_news})

@app.route('/newsByCity', methods=['POST'])
def getNewsByCity():
	city = request.form['city']
	all_news = []
	for pos in Position.select().where(Position.city == city):
		if pos.news.count() != 0:
			news = pos.news[0];
			all_news.append({'lat': pos.lat, 'lng': pos.lng, 'title': news.title.encode('utf-8'), 'link': news.link, 'desc': news.desc.encode('utf-8')})
	print len(all_news)
	return jsonify({'news': all_news})
