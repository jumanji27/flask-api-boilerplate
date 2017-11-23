from flask import jsonify, request

from api.init import db, api
from api.v1.models.users import Users, Schema as UsersSchema


@api.route('/', methods=['GET'])
def main():
    return jsonify({'greeting': "Hello, I'm API"})


@api.route('/api/map', methods=['POST'])
def map():
    methods = {}

    for rule in api.url_map.iter_rules():
        if rule.endpoint != 'static':
            methods[rule.rule] = api.view_functions[rule.endpoint].__doc__

    return jsonify(methods)


@api.route('/api/v1/get', methods=['POST'])
def get():
    schema = UsersSchema(many=True)

    return jsonify(
        success=schema.dump(Users.query.all()).data
    )


@api.route('/api/v1/set', methods=['POST'])
def set():
    db.session.add(
        Users(
            request.json['name'],
            request.json['profession'],
        )
    )
    db.session.commit()

    return jsonify({'success': True})
