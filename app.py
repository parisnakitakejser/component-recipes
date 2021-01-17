import os
import logging
import dotenv

from project.flask import create_app

dotenv.load_dotenv()
debug_mode = True if os.getenv('DEBUG_MODE') == '1' else False

if debug_mode:
    logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', '5000', debug=debug_mode)