from flask import render_template, Blueprint
from flask_socketio import emit
from app import socketio


base = Blueprint("base", __name__)

@base.route('/')
@base.route('/index')
def index():
    return render_template("index.html")

@socketio.on('connect')
def joined(message=None):
    """Sent by clients when they request a connection. """
    emit('connect', {'data': 'connected'})

@socketio.on('clientHello')
def joined(message=None):
    """Sent by clients when they establish a full connection. """
    emit('serverHello', {'data': 'connected'})

