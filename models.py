from datetime import datetime
import connect
from mongoengine import EmbeddedDocument, Document
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

# Quotes.register_delete_rule(Authors, 'fullname', StringField)