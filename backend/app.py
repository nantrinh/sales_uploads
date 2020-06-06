import time
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# format: postgresql://user:password@hostname/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:password@localhost:5432/sales"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# import here to prevent circular reference
import models
import helper

db.create_all()

@app.route('/', methods=['GET'])
def hello():
    return 'Hello world'

@app.route('/sales', methods=['POST'])
def upload_sales():
   data = request.get_data(as_text=True)
   parsed = helper.parse(data)
   helper.persist(parsed['sales'])
   return jsonify({'num_rows': parsed['num_rows'],
                   'revenue': parsed['revenue']})

# automatically import these items into flask shell
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=models.User, Sale=models.Sale)