from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True)
app.host = 'localhost'
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@socketio.on("chat")
def handle_chat(data):
    emit("chat", data, broadcast=True)


@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('change')
def handle_change(state):
    print("Endpoint called.")
    emit('change', state, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=0.0)
