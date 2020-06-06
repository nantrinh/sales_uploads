from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

import os

print(f"XXXXXX Current working path: {os.getcwd()} XXXXXXX")

from app import db

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
    created_on = db.Column(db.Time(timezone=True), nullable=False, default=func.now()) 

    def __repr__(self):
        return f'<Sale {self.customer_name} {self.description} {self.price} {self.quantity}'
