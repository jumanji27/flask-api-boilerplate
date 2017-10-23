import os


dirname = os.path.dirname(__file__)
basedir = os.path.abspath(dirname)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask-simple-api'
    HOST = '0.0.0.0'
    PORT = 5000


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
