# Models and associated schema
import app
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON
from flask_marshmallow import Marshmallow

# Initialize Marshmallow
ma = Marshmallow(app)

db = app.db
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
