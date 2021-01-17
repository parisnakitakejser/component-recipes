import logging
from flask import Response, request
from bson.json_util import dumps, loads

from library.odm.ingredients import Ingredients as OdmIngredients, IngredientsBarcode as OdmIngredientsBarcode

class FlaskIngredients:
    @staticmethod
    def getAll():
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(OdmIngredients.objects().to_json())
        }), mimetype='text/json'), 200
    
    @staticmethod
    def get(id: str):
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(OdmIngredients.objects.get(pk=id).to_json())
        }), mimetype='text/json'), 200

    @staticmethod
    def insert():
        data = request.get_json()

        ingredient = OdmIngredients()
        ingredient.name = data.get('name')

        if data.get('barcode'):
            barcode = data.get('barcode')
            ingredient.barcode = OdmIngredientsBarcode()
            ingredient.barcode.ean13 = barcode.get('ean13')

        ingredient.save()

        return Response(dumps({
            'status': 'Success',
            'resualt': {
                '_id': ingredient.pk
            }
        }), mimetype='text/json'), 200