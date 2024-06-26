import connect
from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField, ListField
class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors)
    quote = StringField()