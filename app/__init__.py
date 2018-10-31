from flask import Flask
from flasgger import Swagger, swag_from
from app.config import app_config
from app.main.errors.request_errors import RequestError


def create_app(config_class):
    """
    This class creates a new Flask object and
    registers its configurations.
    """
    app = Flask(__name__)
    app.config.from_object(app_config[config_class])
    app.config['SWAGGER'] = {
        'title': 'Store Manager API',
        'universion': 3
    }

    swagger = Swagger(app)

    # Request Exceptions
    app.errorhandler(404)(RequestError.not_found)
    app.errorhandler(405)(RequestError.method_not_allowed)

    # Register blueprints
    from app.main.index import api as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/api/v1')

    from app.main.auth import api as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth')

    from app.main.attendant import api as attendant_blueprint
    app.register_blueprint(attendant_blueprint, url_prefix='/api/v1/auth')

    return app
