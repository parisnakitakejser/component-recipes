from mongoengine import Document, StringField

class Units(Document):
    name_short = StringField(primary_key=True)
    name_long = StringField()