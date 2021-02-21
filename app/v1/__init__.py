# Library imports
from flask import Blueprint
from flask_restx import Api, apidoc

from app import CORS

# Init Blueprint
v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

# Init Cors on blueprint
CORS(v1)

# Importing the namespaces.
from .namespaces.migrations import api_migration as migration_namespace
from .namespaces.sandbox import sandbox_api as sandbox_namespace

# Authorization dictionary
authorizations = {
    "apikey": {"in": "header", "type": "apiKey", "name": "x-access-token"}
}
description = """
This is <b>momo api</b> REST API for mobile money transfers.
 All request in regards to the application can be found here,
in general most of the methods require you being as an active user to be able to access.
"""

# Init api.
api = Api(
    v1,
    title="Momo API",
    authorizations=authorizations,
    description=description,
    version="1.0",
    doc="/doc/",
    base_url="/",
    default="migrations",
    default_label="migrations namespace.",
)


@api.documentation
def swagger_ui():
    print("DANS LA DOC")
    return apidoc.ui_for(api)


# Registering namespaces to the api.
api.add_namespace(migration_namespace)
api.add_namespace(sandbox_namespace)
