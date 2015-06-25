from LBRSS_WS import app
from flask import render_template, flash, request, g, session, redirect, url_for
from crawl import crawl
from tables import News, Position

@app.route('/', methods=['GET'])
def hello():
	for pos in Position.select():
		print pos.country
	return 'Hello, world!'
