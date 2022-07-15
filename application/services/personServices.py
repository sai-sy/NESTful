from flask import current_app
import requests
from sqlalchemy import distinct

from .. import db
from ..models.person import Person
from ..schema.personSchema import person_schema

def find_gov_level(arr, level) -> int:
    '''Given a list of dictionaries, find the correct element representing the currect level of government and returns the index'''
    if level == 'provincial' or level == 'p':
        for i in arr:
            if 'Legislative Assembly of Ontario' in i.keys():
                return i
            else:
                continue
        return -1
    elif level == 'federal':
        for i in arr:
            if 'House of Commons' in i.keys():
                return i
            else:
                continue
        return -1

def postal_to_riding(postal_code: str, level) -> str:
    ON = "https://represent.opennorth.ca/postcodes/"
    postal_code_mutt = postal_code.replace(" ", "").upper()
    response = requests.get(ON + postal_code_mutt)
    d = response.json()
    arr = d['representatives_centroid']
    di = arr[find_gov_level(arr, level)]
    district =  di['district_name']
    return district

def person_factory(payload: dict):
    person: Person = person_schema.load(payload)
    current_app.logger.info('past the load')
    person.riding = postal_to_riding(person.postal_code, 'p')
    current_app.logger.info('past the riding')
    persons: list = Person.query.filter_by(email=payload["email"]).all()
    current_app.logger.info('past the changes')
    if len(persons) < current_app.config.get("MAX_ACCOUNTS_UNDER_EMAIL"):
        db.session.add(person)
        db.session.commit()

        return {'message': 'Person Information Successfully Added', 'Info': person_schema.dump(person)}, 201

    else:
        current_app.logger.info(len(persons))
        return {'message': 'There are too many accounts under this email'}, 406
