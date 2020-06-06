from app import db
from models import Sale

def parse(data):
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
    return {'num_rows': num_rows, 'revenue': round(revenue, 2), 'sales': sales}


def persist(sales):
    db.session.add_all(sales)
    db.session.commit()