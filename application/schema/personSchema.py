import email
from marshmallow import Schema, fields, post_dump, post_load
from ..models.person import Person

class PersonSchema(Schema):
    email = fields.String(required=True)
    postal_code = fields.String()
    riding = fields.String()


    class Meta:
        fields = ("id", "email", "first_name", "last_name", "postal_code", "riding")

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)