# Lib imports
import os

from flask import Flask, render_template, jsonify, request
from flask_alembic import Alembic
from flask_caching import Cache
from flask_compress import Compress
from flask_cors import CORS
from flask_language import Language, current_language
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
# from plaid import Client
# from elasticapm.contrib.flask import ElasticAPM
# from elasticsearch import Elasticsearch
from werkzeug.middleware.proxy_fix import ProxyFix

from config import config

# from keycloak import KeycloakOpenID, KeycloakAdmin
# from twilio.rest import Client as TwilioClient

# Library declarative.
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
manager = Manager()
alembic = Alembic()
mail = Mail()
cache = Cache()
# celery = Celery()
# redis = Redis()
language = Language()
compress = Compress()
# apm = ElasticAPM()
Config = config[os.getenv('APP_ENV', "DEVELOPMENT")]


def create_app(environment):
    # Init flask
    app = Flask(__name__, static_folder='./static',
                template_folder='./templates')

    # Init flask configurations.
    app.config.from_object(config[environment])
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # Enabling the cross origin using the cors.
    CORS(app)

    # Attach celery
    # celery.config_from_object(config[environment])

    # Init flask Alembic
    alembic.init_app(app)

    # Init mailRedis
    mail.init_app(app)

    # Init SQLAlchemy.
    with app.app_context():
        db.init_app(app)

    # Init Marshmallow.
    with app.app_context():
        ma.init_app(app)

    # Init flask compress
    with app.app_context():
        compress.init_app(app)

    # Init application migrations (Flask-Migrate and Flask-Script)
    with app.app_context():
        migrate.init_app(app, db)
    with app.app_context():
        manager.__init__(app)
        manager.add_command('database', MigrateCommand)
#    # Init Elasticsearch
#    # with app.app_context():
#    #     es.init_app(app)
#
    # Init Flask Cache
    with app.app_context():
        cache.init_app(app)

    # Init Flask Redis
    with app.app_context():
        # redis.init_app(app)
        cache.init_app(app)

    # Init Flask apm for logging error on elasticsearch
    # try:
    #     with app.app_context():
    #         apm.init_app(app)
    # except Exception as e:
    #     print(str(e))

    # Init Flask-Language
    with app.app_context():
        language.init_app(app)

    @language.allowed_languages
    def get_allowed_languages():
        return ['en', 'fr']

    @language.default_language
    def get_default_language():
        return 'en'

    @app.route('/api/language')
    def get_language():
        return jsonify({
           'language':str(current_language)
        })

    @app.route('/api/language', methods=['POST'])
    def set_language():
        req = request.get_json()
        lang = req.get('language', None)
        language.change_language(lang)
        return jsonify({
            'language': str(current_language)
        })

    # Importing and registering blueprints.
    from .v1 import (v1)
    app.register_blueprint(v1)
    # Sample HTTP error handling

    # Registering blueprints.
    from .public import public_blueprint
    app.register_blueprint(public_blueprint)

    # Init server name to blueprint
    # with app.app_context():
    #    assert url_for('api_v1.doc')

    # Sample HTTP error handling
    @app.errorhandler(404)
    def not_found(error):
        return render_template('v1/404.html'), 404

    return app

