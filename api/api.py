import time
from flask import Flask, request, jsonify
from persist import Sale, persist

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello world'

@app.route('/sales', methods=['POST'])
def upload_sales():
    data = request.get_data(as_text=True)
    data = [line.strip().split(',') for line in data.split('\n') if len(line)]

    # assume the columns arrive ordered and all columns have values
    # customer_name, description, price, quantity, merchant_name, merchant_address
    fields = ['customer_name', 'description', 'price',
              'quantity', 'merchant_name', 'merchant_address']

    num_rows = len(data[1:])
    revenue = 0
    sales = []
    for line in data[1:]:
        sales.append(Sale(**dict(zip(fields, line))))
        revenue += float(sales[-1].price) * int(sales[-1].quantity)
    persist(sales)
    return jsonify({'num_rows': num_rows, 'revenue': round(revenue, 2)})