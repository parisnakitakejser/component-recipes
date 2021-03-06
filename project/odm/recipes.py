from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, FloatField, IntField, ListField, ReferenceField
from project.odm.tags import Tags
from project.odm.ingredients import Ingredients
from project.odm.units import Units

class RecipesIngredients(EmbeddedDocument):
    ingredients = ReferenceField(Ingredients, dbref=True)
    unit_id = ReferenceField(Units, dbref=True)
    qty = FloatField()

class Recipes(Document):
    user_key = StringField()

    title = StringField()
    url = StringField()
    procedure = StringField()
    durability = IntField()
    number_of_people = IntField()
    working_time = IntField()
    total_time = IntField()

    tags = ListField(ReferenceField(Tags, dbref=True))
    ingredients = ListField(EmbeddedDocumentField(RecipesIngredients))
