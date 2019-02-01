# Models and associated schema

from datetime import datetime
from app import db, ma
from sqlalchemy.dialects.postgresql import JSON

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), index=True)
    fname = db.Column(db.String(32))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, lname, fname, created_at, updated_at):
        self.lname = lname
        self.fname = fname
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session
