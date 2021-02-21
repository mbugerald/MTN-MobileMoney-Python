# Import
from ..namespaces.migrations import api_migration
from flask_restx import fields

# List of models
access_key = api_migration.model('migrations access key', {
    "access_key": fields.String(description="expected access key")
})

# Create database model
create_database = api_migration.inherit('creating database model', access_key, {
    "database_name": fields.String(description="Name of the expected database")
})

# handler for migrate sql dumps
create_sql_dumps = api_migration.inherit('dump sql files', access_key, {
    "filename": fields.String(description="expected file name")
})
