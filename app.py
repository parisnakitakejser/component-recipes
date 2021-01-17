import os
import logging
from flask import Flask
import dotenv

from library.middleware.dbConnect import DBConnect
from library.middleware.authService import AuthService

from library.flask.recipes import FlaskRecipes
from library.flask.groups import FlaskGroups
from library.flask.ingredients import FlaskIngredients
from library.flask.units import FlaskUnits
from library.flask.tags import FlaskTags

dotenv.load_dotenv()
debug_mode = True if os.getenv('DEBUG_MODE') == '1' else False

if debug_mode:
    logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
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
app.add_url_rule('/ingredients/:id', view_func=FlaskIngredients.get, endpoint='ingredients_get', methods=['GET'])

app.add_url_rule('/units', view_func=FlaskUnits.getAll, endpoint='units_get_all', methods=['GET'])
app.add_url_rule('/units/:id', view_func=FlaskUnits.get, endpoint='units_get', methods=['GET'])

app.add_url_rule('/tags', view_func=FlaskTags.get, endpoint='tags_get_all', methods=['GET'])
app.add_url_rule('/tags/:id', view_func=FlaskTags.getAll, endpoint='tags_get', methods=['GET'])


if __name__ == '__main__':
    app.run('0.0.0.0', '5000', debug=debug_mode)