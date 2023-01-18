from flask import Flask, request
from flask_cors import CORS
from game import Game

from play import Play
from game import Game
import time



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
    data = request.get_json()
    game = Game(data["player"])
  
    test = Play()
    # game = Game(1)
    player = 1
    while (not game.gameOver()):
        if (player == 1):            
            player, newState = test.humanTurn(game, data["fosse"])
        else:
            player, newState = test.computerTurn(game, test)
            
            time.sleep(1)
        
    time.sleep(10)

    print(newState)
    
    return game


app.run()
