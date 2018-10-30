import unittest
from flask_script import Manager
from app import create_app
from app.db import Database

db = Database()
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

@manager.command
def drop_all():
    """
    Command to drop all database tables.
    """
    db.drop_tables()


if __name__ == "__main__":
    db.create_tables()
    manager.run()
