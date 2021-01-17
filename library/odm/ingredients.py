from mongoengine import Document, StringField, ReferenceField
from library.odm.units import Units

class Ingredients(Document):
    name = StringField(required=True)
    barcode_ean13 = StringField(required=False, max_length=13, min_length=13)