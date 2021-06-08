from flask import Flask, jsonify;
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'yoo this is a secret. shhhhh!'

socketIo = SocketIO(app)

@app.route('/')
def status():
   return jsonify({"message":"Server is running!"})

@socketIo.on("message")
def handleMessage(msg):
    send(msg, broadcast=True)
    return None

if __name__ == '__main__':
    socketIo.run(app , debug=True)