from marshmallow import Schema, fields

from api.init import db


class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

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
