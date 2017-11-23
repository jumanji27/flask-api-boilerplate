from flask import jsonify, request

from api.init import db, api
from api.v1_1.models.users import Users, Schema as UsersSchema

from api.v1.routes import init as v1


@api.route('/api/v1.1/get', methods=['POST'])
def get1():
    return v1.get()


@api.route('/api/v1.1/set', methods=['POST'])
def set1():
    return v1.set()
