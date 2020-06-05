import time
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sales', methods=['POST'])
def upload_sales():
    data = request.get_data(as_text=True)
    data = [line.strip().split(',') for line in data.split('\n')]
    print(data)
    print("\n\n")
    print(data[0])

    # get indexes of quantity and price
#     quantity_index =
#     price_index = 
#    for field in data[0]:
#        if 'price' in field.lower():

    num_rows = len(data[1:])
    revenue = 0

    for line in data[1:]:
        print(line)
    return jsonify({'num_rows': 20, 'revenue': 100})