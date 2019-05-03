from flask import Flask, request
from flask_cors import CORS
import pygal
from pygal.style import DefaultStyle
import urllib.request, html, urllib.parse
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

@app.route("/<quarter>/<year>/<code>", methods=['GET'])
def main(quarter, year, code):
	bu = "https://www.ics.uci.edu/~rang1/{}{}/{}.txt"
	bu2 = "https://www.ics.uci.edu/~abakis/{}{}/{}.txt" # NEW
	try:
		with urllib.request.urlopen(bu.format(quarter, year, code)) as inf:
			src = inf.read().decode('utf-8')

		with urllib.request.urlopen(bu2.format(quarter, year, code.lstrip('0'))) as inf: # NEW
			description = inf.read().decode('utf-8') #NEW

	except:
        	description = 'We do not have data on this section! Maybe because this section was added in late or got canceled or doesn\'t exist!'

		chart = pygal.Line(no_data_text='Course Not Found',
		style=DefaultStyle(no_data_font_size=40))
		chart.add('line', [])
		src = chart.render_data_uri()

	client_agent = request.user_agent
	if client_agent.browser.strip() == 'msie' or 'Edge' in client_agent.string:
		return '<p>{}</p><img id="cheerio" src={} />'.format(description, src) # NEW
	else:
		return '<p>{}</p><embed id="cheerio" type="image/svg+xml" src= {} />'.format(description, src) # NEW
