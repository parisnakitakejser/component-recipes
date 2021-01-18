import os
from flask import url_for
from bson.json_util import dumps, loads
import logging

from project.flask import create_app

from project.odm.groups import Groups as OdmGroups

def test_groups_get_all():
    OdmGroups.drop_collection()

    app = create_app()

    groups = OdmGroups()
    groups.name = 'Dinner'
    groups.save()

    groups = OdmGroups()
    groups.name = 'Breakfast and Brunch'
    groups.save()

    groups = OdmGroups()
    groups.name = 'Lunch'
    groups.save()

    response = app.test_client().get("/groups")
    assert response.status_code == 200

    json_data = loads(response.get_data(as_text=True))
    assert len(json_data['resualt']) == 3

def test_groups_insert():
    OdmGroups.drop_collection()
    
    app = create_app()

    response = app.test_client().post("/groups", data=dumps({
        "name": "Lunch"
    }), headers={'Content-Type': 'application/json'})
 
    json_data = loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert json_data['status'] == 'Success'

    id = json_data['resualt']['_id']
    row = OdmGroups.objects.get(pk=id)

    assert row.name == 'Lunch'