from init import db
from marshmallow import Schema, fields


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    profession = db.Column(db.String())

    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Schema(Schema):
    class Meta:
        fields = ('id', 'name', 'profession')
