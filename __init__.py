from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socket = SocketIO(app, logger=True)

import routes