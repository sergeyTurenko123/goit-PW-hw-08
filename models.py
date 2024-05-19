from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField

class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

# class Quotes:
#     tags = StringField()
#     author = StringField()
#     quote = StringField()