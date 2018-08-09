from flask import Flask, request
from flask_cors import CORS
import bcrypt

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST'])
def helloWorld():
    quater = request.form['quarter']
    year = request.form['year']
    code = request.form['code']
    
	bu = os.environ.get('PORTOFCALL')
    
	try:
		with urllib.request.urlopen(bu.format(quarter, year, code)) as inf:
            src = inf.read().decode('utf-8')
	except:
		chart = pygal.Line(no_data_text='Course Not Found',
			   style=DefaultStyle(no_data_font_size=40))
		chart.add('line', [])
		src = chart.render_data_uri()
	
    if client_agent.browser.strip() == 'msie' or 'Edge' in client_agent.string:
    	return '<img src={} />'.format(src)
    else:
        return '<embed type="image/svg+xml" src= {} />'.format(src)
  
