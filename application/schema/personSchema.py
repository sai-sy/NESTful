from .. import ma

class PersonSchema(ma.Schema):
    class Meta:
        fields = ("first_name", "email", "likes")

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)