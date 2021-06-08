from flask import Flask, jsonify;
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoo this is a secret. shhhhh!'

socketIo = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
def status():
   return jsonify({"message":"Server is running!"})

@socketIo.on("message")
def handleMessage(msg):
    socketIo.emit("renderer",msg)

if __name__ == '__main__':
    socketIo.run(app , debug=True)