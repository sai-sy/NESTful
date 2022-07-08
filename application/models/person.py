from flask_restful import Resource
from sqlalchemy import ForeignKey
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum, auto


class Person(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    email = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    # address
    # date_of_birth
    ## day
    ## month
    ## year
    #phone
    # country
    # city