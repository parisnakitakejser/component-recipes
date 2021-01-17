from flask import url_for
import logging

from project.flask import create_app

def test_groups():
    app = create_app()

    response = app.test_client().get('/groups')
    assert response.status_code == 200