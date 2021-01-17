import logging
from flask import Response, request
from bson.json_util import dumps, loads

from project.odm.groups import Groups as OdmGroups

class FlaskGroups:
    @staticmethod
    def getAll():
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(OdmGroups.objects().to_json())
        }), mimetype='text/json'), 200
    
    @staticmethod
    def get(id: str):
        return Response(dumps({
            'status': 'Success',
            'resualt': loads(OdmGroups.objects.get(pk=id).to_json())
        }), mimetype='text/json'), 200
    
    @staticmethod
    def insert():
        data = request.get_json()

        group = OdmGroups()
        group.name = data.get('name')
        group.save()

        return Response(dumps({
            'status': 'Success',
            'resualt': {
                '_id': group.pk
            }
        }), mimetype='text/json'), 200