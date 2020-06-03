import time
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/sales', methods=['POST'])
def upload_sales():
    return NotImplementedError

@app.route('/sales/revenue', methods=['GET'])
def revenue():
    return NotImplementedError

@app.route('/time')
def get_current_time():
    return {'time': time.time()}