from mongoengine import Document, StringField, IntField, ListField, ReferenceField
from project.odm.tags import Tags
from project.odm.ingredients import Ingredients

class RecipesIngredients(Documents):
    ingredients = ReferenceField('Ingredients')
    unit_id = ReferenceField('Units')

class Recipes(Document):
    user_key = StringField()

    title = StringField()
    url = StringField()
    procedure = StringField()
    durability = IntField()
    number_of_people = IntField()
    working_time = IntField()
    total_time = IntField()

    tags = ListField(ReferenceField('Tags'))
    ingredients = ListField(EmbeddedDocumentField(RecipesIngredients))
