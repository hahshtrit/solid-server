from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.secret_key = b'key'
socket = SocketIO(app, logger=True)

import routes