# Library imports.
import os

from app import db
from config import Base

# from app import apm, celery, some_queue


current_dir = os.path.dirname(os.path.realpath(__file__))
# Applications migrations middleware used to migrate the database, update and create start point users
# Init user is bara_admin@bara.ca as email and password is bara2018


class Migrations:
    def __init__(self):
        pass

    # Performing Flask-Migrations init function to create required dependencies.
    # Executable only once by the admin (Super level expected to handle this.)
    @staticmethod
    # @celery.task(name='init.task')
    def init(args):
        try:
            if args["access_key"] != Base.SECURITY_KEY:
                return {"message": "Invalid authorization"}, 401
            os.system('python manage.py database init')
            return {'message': 'init done'}, 200
        except Exception as e:
            # apm.capture_exception()
            return {'message': str(e)}, 500
        except:
            return {'message': 'Conflict, Already created!'}, 409

    # Committing create SQLAlchemy models to the existing database.
    # Expected auto generation of unique key files with id's.
    # On commit or change update of a model when run the database will assume the changes.
    @staticmethod
    def upgrade(args):
        try:
            if args["access_key"] != Base.SECURITY_KEY:
                return {"message": "Invalid authorization"}, 401
            os.system(
                'python manage.py database upgrade')
            return {'message': 'Updated database!'}, 201
        except Exception as e:
            # apm.capture_exception()
            db.session.rollback()
            return {'message': str(e)}, 500

    @staticmethod
    def migrate(args):
        try:
            if args["access_key"] != Base.SECURITY_KEY:
                return {"message": "Invalid authorization"}, 401
            os.system(
                'python manage.py database migrate')
            return {'message': 'Migrated database!'}, 201
        except Exception as e:
            # apm.capture_exception()
            db.session.rollback()
            return {'message': str(e)}, 500

    @staticmethod
    def downgrade(args):
        try:
            if args["access_key"] != Base.SECURITY_KEY:
                return {"message": "Invalid authorization"}, 401
            os.system(
                'python manage.py database downgrade')
            return {'message': 'Downgraded database!'}, 201
        except Exception as e:
            # apm.capture_exception()
            db.session.rollback()
            return {'message': str(e)}, 500
