from tables import News, Position
from flask import Flask, g

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LBRSS_WS'

from LBRSS_WS import map_news

