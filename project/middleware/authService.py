import os
import logging
from werkzeug.wrappers import Request, Response
from mongoengine import connect

class AuthNotAllowed(Exception):
    pass

class AuthService:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            logging.info('Auth Service success')
            return self.app(environ, start_response)

        except AuthNotAllowed as e:
            logging.info('Auth Service failed')

            res = Response(u'Auth Service failed', mimetype='text/plain', status=401)
            return res(environ, start_response)