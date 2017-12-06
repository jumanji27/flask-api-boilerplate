import os


dirname = os.path.dirname(__file__)
basedir = os.path.abspath(dirname)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgres://db:5432/flask_api_boilerplate'
    HOST = '0.0.0.0'
    PORT = 5000


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
