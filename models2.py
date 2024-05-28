import connect
from mongoengine import Document
from mongoengine.fields import BooleanField, StringField, EmailField

class Contact(Document):
    name = StringField()
    email =EmailField()
    log =BooleanField()
