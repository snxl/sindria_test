import logging

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.exceptions import HTTPException
from werkzeug.middleware.proxy_fix import ProxyFix

from src.routes.index import Routes

load_dotenv()


class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.load_before_middlewares()
        self.load_routes()
        self.load_after_middlewares()

    def load_before_middlewares(self):
        CORS(self.app, origins='*', supports_credentials=True)

        @self.app.route('/favicon.ico')
        def favicon():
            return '', 204

        self.app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)

        swagger_url = '/api-docs'
        api_url = '/static/swagger.json'

        swagger_blueprint = get_swaggerui_blueprint(
            swagger_url,
            api_url,
            config={
                'app_name': 'sindria doc'
            }
        )
        self.app.register_blueprint(swagger_blueprint, url_prefix=swagger_url)

    def load_after_middlewares(self):
        @self.app.errorhandler(Exception)
        def handle_error(error):
            if isinstance(error, HTTPException):
                return jsonify(status='error', message=error.description), error.code
            else:
                logging.exception('Exception: %s', str(error))
                return jsonify(status='error', message='Internal Server Error'), 500

    def load_routes(self):
        Routes().load(self.app)
