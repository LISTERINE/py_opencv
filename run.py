from app import create_app, socketio
import os
from flask_socketio import SocketIO

env = os.environ.get("APPNAME", "prod")
app = create_app('app.settings.{}Config'.format(env.capitalize()), env=env)

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=80)
