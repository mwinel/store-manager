from flask import Flask
from app.config import app_config
from app.main.errors.request_errors import RequestError


def create_app(config_class):
    """
    This class creates a new Flask object and
    registers its configurations.
    """
    app = Flask(__name__)
    app.config.from_object(app_config[config_class])

    # Request Exceptions
    app.errorhandler(404)(RequestError.not_found)
    app.errorhandler(405)(RequestError.method_not_allowed)
    app.errorhandler(500)(RequestError.internal_server_error)

    # Register blueprint
    from app.main.index import api as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/api/v1')

    return app
