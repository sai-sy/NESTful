from http.client import BAD_REQUEST
from flask import Blueprint, request, abort, current_app

from .. import db
from ..models.person import Person
from ..schema.personSchema import person_schema, persons_schema
from ..services.personServices import person_factory

personRoute = Blueprint('personRoute', __name__)

@personRoute.route("/persons/email/<person_email>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def persons_by_email(person_email):
    if request.method == 'POST':
        payload = request.json
        current_app.logger.info(payload)
        errors = person_schema.validate(payload)
        if errors:
            current_app.logger.info('error')
            abort(BAD_REQUEST, str(errors))
        else:
            current_app.logger.info('into the else')
            return person_factory(request.json)
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        person:Person = Person.query.filter_by(email=person_email).all()
        return persons_schema.dump(person), 200
    
    return "Hello, World!"

@personRoute.route("/persons/id/<person_id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def persons_by_id(person_id):
    if request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        person:Person = Person.query.filter_by(id=person_id).first()
        return person_schema.dump(person), 200