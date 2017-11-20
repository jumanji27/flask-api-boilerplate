from flask import jsonify, request

from models.init import db, app
from models.users import Users, Schema as UsersSchema


@app.route('/', methods=['GET'])
def main():
    return jsonify({'greeting': "Hello, I'm API"})


@app.route('/api/v1/get', methods=['POST'])
def get():
    schema = UsersSchema(many=True)

    return jsonify(
        success=schema.dump(Users.query.all()).data
    )


@app.route('/api/v1/set', methods=['POST'])
def set():
    db.session.add(
        Users(
            request.json['name'],
            request.json['profession'],
        )
    )
    db.session.commit()

    return jsonify({'success': True})


@app.route('/api/map', methods=['POST'])
def map():
    methods = {}

    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            methods[rule.rule] = app.view_functions[rule.endpoint].__doc__

    return jsonify(methods)