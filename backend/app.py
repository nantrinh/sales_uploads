from flask import Flask, request, jsonify
from flask_cors import cross_origin

from api.models import db, User, Sale, parse, persist

app = Flask(__name__)

# format: postgresql://user:password@hostname/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:password@postgres:5432/sales"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)
db.create_all()


@app.route('/', methods=['GET'])
def hello():
    return 'Hello world'


# TODO: need to add configs to change cross origin restrictions when testing
@app.route('/sales', methods=['POST'])
@cross_origin('http://frontend.com')
def upload_sales():
    # TODO: stream data in chunks
    data = request.get_data(as_text=True)
    parsed = parse(data)
    persist(parsed['sales'])
    return jsonify({'num_rows': parsed['num_rows'],
                    'revenue': parsed['revenue']})

# automatically import these items into flask shell, for ease of debugging


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Sale=Sale)


if __name__ == "__main__":
    # need to bind to all IPs
    app.run(host='0.0.0.0')
