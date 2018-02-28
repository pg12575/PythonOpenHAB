from flask import Flask
from config import Config
import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config.from_object(Config)

async_mode=None
socketio = SocketIO(app, async_mode=async_mode)

from app import routes