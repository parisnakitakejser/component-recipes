from mongoengine import Document, StringField

class Units(Document):
    name_short = StringField()
    name_long = StringField()