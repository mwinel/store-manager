from flask import current_app
from manage import app
from app.tests.base import BaseTestCase


class TestDevelopmentConfig(BaseTestCase):
    """Test development enviroment configurations."""

    def create_app(self):
        app.config.from_object('app.config.DevelopmentConfig')
        return app

    def test_development_enviroment(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(BaseTestCase):
    """Test testing enviroment configurations."""

    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def test_testing_enviroment(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is False)


class TestProductionConfig(BaseTestCase):
    """Test production enviroment configurations."""

    def create_app(self):
        app.config.from_object('app.config.ProductionConfig')
        return app

    def test_production_enviroment(self):
        self.assertTrue(app.config['TESTING'] is False)
        self.assertTrue(app.config['DEBUG'] is True)
