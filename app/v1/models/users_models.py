from ..namespaces.sandbox import sandbox_api
from flask_restx import fields


# customer payment request
collect_customer_payment = sandbox_api.model("collect customer payments", {
    "amount": fields.String(description="expected amount.", required=True),
    "currency": fields.String(default="EUR", description="expected currency ISO format", required=True),
    "external_id": fields.String(description="expected customer's phone number.", required=False),
    "phone_number": fields.String(description="expected phone number or identification of the user", required=True),
    "payer_message": fields.String(description="expected message to be sent to the user.", required=True),
    "payer_note": fields.String(description="expected not to be sent to the user", required=True),
})

# Create collection users.
create_collection_users = sandbox_api.model("create collection users", {
    "provider_callback_host": fields.String(
        description="expected callback url",
        required=True
    ),
})

# Obtain collection api key.
create_collection_api_key = sandbox_api.model("obtain collection api key", {
    "x_reference_id": fields.String(
        description="expected x_reference id uuid 4",
        required=True
    )
})
