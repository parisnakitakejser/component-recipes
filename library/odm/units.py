from mongoengine import Document, StringField

class Units(Document):
    name_long = StringField()
    name_short = StringField()