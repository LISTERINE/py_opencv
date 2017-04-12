from os import path

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))

    # mimetypes to compress
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript', 'image/svg+xml']


class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass
