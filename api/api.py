import time
from flask import Flask, request

app = Flask(__name__)

@app.route('/sales', methods=['POST'])
def upload_sales():
    data = request.get_data(as_text=True)
    data = [line.strip().split(',') for line in data.split('\n')]
    print(data)
    print("\n\n")
    print(data[0])
    for line in data[1:]:
        print(line)
    return 'Submitted form' 