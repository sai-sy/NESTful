from .. import db
from flask_restful import Api, Resource, reqparse, abort


class Video(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)