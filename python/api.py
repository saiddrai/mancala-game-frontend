from flask import Flask , request

PORT = 5000


app = Flask(__name__)

# configure listening port
app.config['SERVER_NAME'] = f'localhost:{PORT}'


@app.route('/')
def hello_world():
    return 'Hello, World!'

# a post request to /api/echo with a JSON body {"echo": "some text"} will return the same JSON body

@app.route('/api/echo', methods=['POST'])
def echo():
    return request.get_json()

app.run()