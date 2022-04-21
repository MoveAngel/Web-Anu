from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null
from app import db

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    nim = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    prodi = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Name: {}>".format(self.name)