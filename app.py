from flask import Flask, request
from flask_cors import CORS
import pygal
from pygal.style import DefaultStyle
import bcrypt
import os
import urllib.request, html, urllib.parse
from urllib.parse import urlparse


app = Flask(__name__)
CORS(app)

@app.route("/<quarter>/<year>/<code>", methods=['GET','POST'])
def main(quarter, year, code):
	bu = os.environ.get('PORTOFCALL')
	try:
		with urllib.request.urlopen(bu.format(quarter, year, code)) as inf:
			src = inf.read().decode('utf-8')
	except:
		chart = pygal.Line(no_data_text='Course Not Found',
		style=DefaultStyle(no_data_font_size=40))
		chart.add('line', [])
		src = chart.render_data_uri()
	
	client_agent = request.user_agent
	if client_agent.browser.strip() == 'msie' or 'Edge' in client_agent.string:
		return '<img id="cheerio" src={} />'.format(src)
	else:
		return '<embed id="cheerio" type="image/svg+xml" src= {} />'.format(src)

