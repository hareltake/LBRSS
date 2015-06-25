from LBRSS_WS import app
from flask import render_template, flash, request, g, session, redirect, url_for
from crawl import crawl

@app.route('/', methods=['GET'])
def hello():
	crawl()
	return 'Hello, world!'
