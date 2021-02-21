# Library imports
from flask_restx import Namespace, Resource, reqparse

from ..controllers.middleware_migrations import Migrations

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# Declaring the namespace for users.
api_migration = Namespace('migrations', description='migrate the database.')

# Import migration models
from ..models.migration_models import (
    access_key
)


# Migrations create default accounts
@api_migration.route("/migrate-default-accounts")
class MigrateDefaultAccount(Resource):
    @api_migration.expect(access_key)
    def post(self):
        """ Pushing default accounts."""
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('access_key', type=str, required=True)
            args = parser.parse_args()
            default_accounts = Migrations.create_default_users(args)
            return default_accounts
        except Exception as e:
            return str(e)


# Migrations create default accounts
@api_migration.route("/migrate-default-roles")
class MigrateDefaultRoles(Resource):
    @api_migration.expect(access_key)
    def post(self):
        """ Migrating application roles."""
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument('access_key', type=str, required=True)
            args = parser.parse_args()
            roles = Migrations.migrate_roles(args)
            return roles
        except Exception as e:
            return str(e)


# Init migrations
@api_migration.route("/create-directory-schema")
class CreateMigrationDirectory(Resource):
    @api_migration.expect(access_key)
    def post(self):
        """ Creating directory for migrations. """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('access_key', type=str, required=True)
        args = parser.parse_args()
        init = Migrations.init(args)
        return init


# migrating sql schema
@api_migration.route("/migrate")
class CreateMigrations(Resource):
    @api_migration.expect(access_key)
    def post(self):
        """ Prepare Sql schema for database upgrade. """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('access_key', type=str, required=True)
        args = parser.parse_args()
        init_migrations = Migrations.migrate(args)
        return init_migrations


# Upgrade database
@api_migration.route("/upgrade-database")
class MigrateToDatabase(Resource):
    @api_migration.expect(access_key)
    def post(self):
        """ Upgrade database. """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('access_key', type=str, required=True)
        args = parser.parse_args()
        upgrade = Migrations.upgrade(args)
        return upgrade


# Downgrade database
@api_migration.route("/downgrade-database")
class DowngradeDatabase(Resource):
    @api_migration.expect(access_key)
    def post(self):
        """ Downgrade database. """
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('access_key', type=str, required=True)
        args = parser.parse_args()
        return Migrations.downgrade(args)
