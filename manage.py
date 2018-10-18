import unittest
from flask_script import Manager
from app import create_app


app = create_app("development")
manager = Manager(app)


@manager.command
def runserver():
    """
    Command to runserver.
    """
    app.run()


@manager.command
def tests():
    """
    Command to run unit tests.
    """
    tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()
