from flask import Flask
from flask_socketio import SocketIO
from secrets import token_urlsafe

app = Flask(__name__)
app.secret_key = token_urlsafe(16).encode()
socket = SocketIO(app, logger=True)

import routes
