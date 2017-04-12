from flask import Flask
from flask_cache import Cache
from flask_compress import Compress
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
from flask_socketio import SocketIO

# Get static assets
from app import assets

from binascii import hexlify
from os import urandom

# init socket context
socketio = SocketIO()

def create_app(config, env="prod"):

    compress = Compress()

    app = Flask(__name__)
    app.config.from_object('config')
    app.config["ENV"] = env
    app.config['SECRET_KEY'] = hexlify(urandom(80))

    # Import and register the different asset bundles
    assets_env = Environment()
    assets_env.init_app(app)
    assets_loader = PythonAssetsLoader(assets)
    for name, bundle in assets_loader.load_bundles().items():
        assets_env.register(name, bundle)

    cache = Cache(app, config={"CACHE_TYPE": "simple"})
    compress.init_app(app)

    socketio.init_app(app)

    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('/var/log/py_opencv/py_opencv.log', 'a',
                                           1 * 1024 * 1024, 10)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('site startup')


    # Register apps
    app.register_blueprint(base_bp)

    return app

# Import blueprints here so everything is already initialized when they load
from app.views.base import base as base_bp
