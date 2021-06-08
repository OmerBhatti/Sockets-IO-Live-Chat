from flask import Flask, jsonify;
from flask_socketio import SocketIO
from flask_cors import cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoo this is a secret. shhhhh!'

socketIo = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
@cross_origin()
def status():
   return jsonify({"message":"Server is running!"})

@socketIo.on("message")
@cross_origin()
def handleMessage(msg):
    socketIo.emit("renderer",msg)

if __name__ == '__main__':
    socketIo.run(app , debug=True)