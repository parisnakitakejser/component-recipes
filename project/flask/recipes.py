import logging
from bson import dbref
from bson.objectid import ObjectId
from flask import Response, request
from bson.json_util import dumps, loads

from project.odm.recipes import Recipes as OdmRecipes, RecipesIngredients as OdmRecipesIngredients 


class FlaskRecipes:
    @staticmethod
    def getAll():
        resualt = OdmRecipes.objects()
        
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(resualt.to_json())
        }), mimetype='text/json'), 200

    @staticmethod
    def get(id: str):
        resualt = OdmRecipes.objects(pk=id).aggregate([{
            '$unwind': '$ingredients'
        }, {
            '$lookup': {
                'from': 'ingredients',
                'foreignField': '_id',
                'localField': 'ingredients.ingredients.$id',
                'as': 'ingredients.ingredients'
            }
        }, {
            '$unwind': '$ingredients.unit_id' 
        }, {
            '$lookup': {
                'from': 'units',
                'foreignField': '_id',
                'localField': 'ingredients.unit_id.$id',
                'as': 'ingredients.unit_id'
            }
        }, { 
            '$addFields': { 
                'ingredients.unit_id': {'$first': "$ingredients.unit_id" } ,
                'ingredients.ingredients': {'$first': "$ingredients.ingredients" }
            }
        }, {
            '$group': {
                '_id': '$_id',
                'ingredients': {'$push': '$ingredients' },
                "title": { "$first": "$title" },
                "url": { "$first": "$url" },
                "procedure": { "$first": "$procedure" },
                "durability": { "$first": "$durability" },
                "number_of_people": { "$first": "$number_of_people" },
                "working_time": { "$first": "$working_time" },
                "total_time": { "$first": "$total_time" },
            }
        }])

        recipe_data = None
        for data in resualt:
            recipe_data = data
            break
 
        return Response(dumps({
            'status': 'Success',
            'resualt': recipe_data
        }), mimetype='text/json'), 200

    @staticmethod
    def replace(id: str):
        pass

    @staticmethod
    def delete(id: str):
        pass

    @staticmethod
    def insert():
        data = request.get_json()

        recipe = OdmRecipes()
        recipe.title = data.get('title')
        recipe.url = data.get('url')
        recipe.procedure = data.get('procedure')
        recipe.durability = data.get('durability')
        recipe.number_of_people = data.get('number_of_people')
        recipe.working_time = data.get('working_time')
        recipe.total_time = data.get('total_time')

        for ingredient in data.get('ingredients'):
            ingredients = OdmRecipesIngredients()
            ingredients.qty = ingredient['qty']
            ingredients.ingredients = ObjectId(ingredient['ingredients'])
            ingredients.unit_id = ObjectId(ingredient['unit_id'])
            recipe.ingredients.append(ingredients) 
    
        recipe.save()

        return Response(dumps({
            'status': 'Success',
            'resualt': {
                '_id': recipe.pk
            }
        }), mimetype='text/json'), 200

    @staticmethod
    def update(id: str):
        pass