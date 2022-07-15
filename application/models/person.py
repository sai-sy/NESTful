from flask_restful import Resource
from sqlalchemy import ForeignKey
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum, auto


class Person(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    code = db.Column(db.String(20))
    
    email = db.Column(db.String(300), nullable=False)
    
    postal_code = db.Column(db.String(12))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    
    riding = db.Column(db.String(150))
    address = db.Column(db.String(1000))
    phone = db.Column(db.String(75))
    

    # date_of_birth
    ## day
    ## month
    ## year
    # country
    # city
