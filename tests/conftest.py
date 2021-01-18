import pytest
from project.flask import create_app

from project.middleware.dbConnect import db_connect
db_connect()

@pytest.fixture
def app():
    app = create_app('flask_test.cfg')
    return app