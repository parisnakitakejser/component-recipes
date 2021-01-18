from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, ReferenceField
from project.odm.units import Units

class IngredientsBarcode(EmbeddedDocument):
    ean13 = StringField(required=False, max_length=13, min_length=13)

class Ingredients(Document):
    name = StringField(required=True)
    barcode = EmbeddedDocumentField(IngredientsBarcode)