from mongoengine import Document, StringField

class Tags(Document):
    user_key = StringField()
    
    name = StringField()