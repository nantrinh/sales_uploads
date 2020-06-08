from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

import os

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    sales = db.relationship('Sale', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.name}'


class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    customer_name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(postgresql.MONEY, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    merchant_name = db.Column(db.String(250), nullable=False)
    merchant_address = db.Column(db.String(250), nullable=False)
    created_on = db.Column(
        db.Time(
            timezone=True),
        nullable=False,
        default=func.now())

    def __repr__(self):
        return f'<Sale {self.customer_name} {self.description} {self.price} {self.quantity}'


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
