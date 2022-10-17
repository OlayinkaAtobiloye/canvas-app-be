from flask import Flask, jsonify
from flask_socketio import SocketIO,join_room
from flask_caching import Cache
from flask_cors import CORS

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True, ping_timeout=5, ping_interval=5,
                    async_handlers=True)
app.host = 'localhost'


@app.route("/")
def index():
    return "This app is up and running"


@socketio.on('send')
def handle_change(data):
    socketio.emit('receive', data["state"], broadcast=True, include_self=False)


if __name__ == '__main__':
    from gevent import monkey
    monkey.patch_all()
    socketio.run(app, debug=True)
