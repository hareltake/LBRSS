from LBRSS_WS import app
from flask import render_template, flash, request, g, session, redirect, url_for
from crawl import crawl
from tables import News, Position

@app.route('/map', methods=['GET'])
def map():
	return  render_template('map.html')

@app.route('/allNews', methods=['GET'])
def getAllNews():
	for pos in Position.select().where(Position.country):
		pass
