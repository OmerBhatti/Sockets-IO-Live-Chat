from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoo this is a secret. shhhhh!'

socketIo = SocketIO(app , cors_allowed_origins="*")

@app.route('/')
def chat():
   return render_template("client.html")

@socketIo.on("message")
def handleMessage(msg):
    socketIo.emit("renderer",msg)

if __name__ == '__main__':
    socketIo.run(app , debug=True)