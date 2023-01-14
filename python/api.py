from flask import Flask, request
from flask_cors import CORS


PORT = 5000


app = Flask(__name__)
CORS(app, supports_credentials=True)
cors = CORS(app, resources={r"/": {"origins": "*"}})

# configure listening port
app.config['SERVER_NAME'] = f'localhost:{PORT}'


@app.route('/')
def hello_world():
    print("helloworld")
    return 'Hello, World!'

# a post request to /api/echo with a JSON body {"echo": "some text"} will return the same JSON body


@app.route('/mancala', methods=['POST'])
def playFoss():
    print(request.get_json())
    return request.get_json()


app.run()
