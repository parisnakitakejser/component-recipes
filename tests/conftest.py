import pytest
from project.flask import create_app

@pytest.fixture
def app():
    app = create_app('flask_test.cfg')
    return app