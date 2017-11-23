import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


def run():
    global db
    global api
    global mm

    api = Flask(__name__)

    api.config.from_object(os.environ['APP_SETTINGS'])
    api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(api)
    mm = Marshmallow(api)
