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


# TODO: restrict CORS except for when testing; need to add configs 
#@cross_origin('http://frontend.com')
@app.route('/sales', methods=['POST'])
@cross_origin()
def upload_sales():
# https://requests.readthedocs.io/en/master/user/quickstart/#raw-response-content
# It is strongly recommended that you open files in binary mode.
# This is because Requests may attempt to provide the
# Content-Length header for you, and if it does this value
# will be set to the number of bytes in the file.
# Errors may occur if you open the file in text mode.
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)
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
