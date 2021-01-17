import os
import dotenv
from flask import Flask

from project.middleware.dbConnect import DBConnect
from project.middleware.authService import AuthService

from project.flask.recipes import FlaskRecipes
from project.flask.groups import FlaskGroups
from project.flask.ingredients import FlaskIngredients
from project.flask.units import FlaskUnits
from project.flask.tags import FlaskTags

dotenv.load_dotenv()
debug_mode = True if os.getenv('DEBUG_MODE') == '1' else False

def create_app(config_filename=None, instance_relative_config=True):
    app = Flask(__name__)
    
    if config_filename is not None:
        app.config.from_pyfile(config_filename)
    
    app.wsgi_app = AuthService(app.wsgi_app)
    app.wsgi_app = DBConnect(app.wsgi_app)

    app.add_url_rule('/recipes', view_func=FlaskRecipes.getAll, endpoint='recipes_get_all', methods=['GET'])
    app.add_url_rule('/recipes/:id', view_func=FlaskRecipes.get, endpoint='recipes_get', methods=['GET'])
    app.add_url_rule('/recipes/:id', view_func=FlaskRecipes.replace, endpoint='recipes_replace', methods=['PUT'])
    app.add_url_rule('/recipes/:id', view_func=FlaskRecipes.delete, endpoint='recipes_delete', methods=['DELETE'])
    app.add_url_rule('/recipes', view_func=FlaskRecipes.insert, endpoint='recipes_insert', methods=['POST'])
    app.add_url_rule('/recipes/:id', view_func=FlaskRecipes.update, endpoint='recipes_update', methods=['PATCH'])

    app.add_url_rule('/groups', view_func=FlaskGroups.getAll, endpoint='groups_get_all', methods=['GET'])
    app.add_url_rule('/groups/<string:id>', view_func=FlaskGroups.get, endpoint='groups_get', methods=['GET'])
    app.add_url_rule('/groups', view_func=FlaskGroups.insert, endpoint='groups_insert', methods=['POST'])

    app.add_url_rule('/ingredients', view_func=FlaskIngredients.getAll, endpoint='ingredients_get_all', methods=['GET'])
    app.add_url_rule('/ingredients/<string:id>', view_func=FlaskIngredients.get, endpoint='ingredients_get', methods=['GET'])
    app.add_url_rule('/ingredients', view_func=FlaskIngredients.insert, endpoint='ingredients_insert', methods=['POST'])

    app.add_url_rule('/units', view_func=FlaskUnits.getAll, endpoint='units_get_all', methods=['GET'])
    app.add_url_rule('/units/<string:id>', view_func=FlaskUnits.get, endpoint='units_get', methods=['GET'])
    app.add_url_rule('/units', view_func=FlaskUnits.insert, endpoint='units_insert', methods=['POST'])

    app.add_url_rule('/tags', view_func=FlaskTags.get, endpoint='tags_get_all', methods=['GET'])
    app.add_url_rule('/tags/:id', view_func=FlaskTags.getAll, endpoint='tags_get', methods=['GET'])

    return app