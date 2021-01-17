import logging
from flask import Response, request
from bson.json_util import dumps, loads

from library.odm.units import Units as OdmUnits

class FlaskUnits:
    @staticmethod
    def getAll():
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(OdmUnits.objects().to_json())
        }), mimetype='text/json'), 200
    
    @staticmethod
    def get(id: str):
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(OdmUnits.objects.get(pk=id).to_json())
        }), mimetype='text/json'), 200

    @staticmethod
    def insert():
        data = request.get_json()

        unit = OdmUnits()
        unit.name_short = data.get('name_short')
        unit.name_long = data.get('name_long')
        unit.save()

        return Response(dumps({
            'status': 'Success',
            'resualt': {
                '_id': unit.pk
            }
        }), mimetype='text/json'), 200