from mongoengine import Document, StringField

class Groups(Document):
    name = StringField()