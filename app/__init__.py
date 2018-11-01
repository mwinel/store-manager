from flask import Flask
from flasgger import Swagger, swag_from
from flask_jwt_extended import JWTManager
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
    app.config['SECRET_KEY'] = "yoyo"
    app.config['JWT_SECRET_KEY'] = "neverrunwithme"
    jwt = JWTManager(app)

    # Request Exceptions
    app.errorhandler(404)(RequestError.not_found)
    app.errorhandler(405)(RequestError.method_not_allowed)

    # Register blueprints
    from app.main.index import api as index_blueprint
    app.register_blueprint(index_blueprint, url_prefix='/api/v1')

    from app.main.auth import api as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1/auth')

    from app.main.product import api as product_blueprint
    app.register_blueprint(product_blueprint, url_prefix='/api/v1/')

    from app.main.sale import api as sale_blueprint
    app.register_blueprint(sale_blueprint, url_prefix='/api/v1/')

    return app
