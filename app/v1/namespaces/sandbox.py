# Library imports
from flask_restx import Namespace, Resource, reqparse

# Declaring the namespace for users.
from ..controllers.middleware_payment import Payment
from ..controllers.middleware_users import Users

sandbox_api = Namespace('sandbox', description='sandbox related operations.')

from ..models.users_models import (
    create_collection_users,
    create_collection_api_key,
    collect_customer_payment
)


@sandbox_api.route('/create/collection/users')
class SandboxCollection(Resource):

    @sandbox_api.doc(security='apikey')
    @sandbox_api.expect(create_collection_users)
    def post(self):
        """ create users under sandbox collection. """
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument("provider_callback_host", type=str, required=False)
            args = parser.parse_args()
            payment = Users.create_collection_users(args)
            return payment
        except Exception as e:
            print("Hello")
            return {"message": str(e)}, 500


@sandbox_api.route('/create/collection/users/apikey')
class SandboxCollectionApiKey(Resource):

    @sandbox_api.doc(security='apikey')
    @sandbox_api.expect(create_collection_api_key)
    def post(self):
        """ create users api key under sandbox collection. """
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument("x_reference_id", type=str, required=False)
            args = parser.parse_args()
            payment = Users.obtain_api_key(args)
            return payment
        except Exception as e:
            print("Hello")
            return {"message": str(e)}, 500


# users parsers
sandbox_collection_api_requestpament = sandbox_api.parser()
sandbox_collection_api_requestpament.add_argument(
    'access_token', type=str, help="access token generated for collection", location='args', required=True
)
sandbox_collection_api_requestpament.add_argument(
    'environment', type=str, default="sandbox", location='args', required=True,
)
sandbox_collection_api_requestpament.add_argument(
    'x_reference_id', type=str, location='args', required=True,
)


@sandbox_api.route('/create/collection/paymentrequest')
class SandboxCollectionPaymentRequest(Resource):

    @sandbox_api.doc(security='apikey')
    @sandbox_api.expect(sandbox_collection_api_requestpament, collect_customer_payment)
    def post(self):
        """ create payment request sandbox collection. """
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument("access_token", type=str, required=True)
            parser.add_argument("environment", type=str, required=True)
            parser.add_argument("x_reference_id", type=str, required=True)
            parser.add_argument("amount", type=str, required=True)
            parser.add_argument("currency", type=str, required=True)
            parser.add_argument("external_id", type=str, required=False)
            parser.add_argument("phone_number", type=str, required=True)
            parser.add_argument("payer_message", type=str, required=True)
            parser.add_argument("payer_note", type=str, required=True)
            args = parser.parse_args()
            payment = Payment.request_collection_payment(args)
            return payment
        except Exception as e:
            print("Hello")
            return {"message": str(e)}, 500


@sandbox_api.route('/create/collection/paymentrequest/status')
class SandboxCollectionPaymentRequestStatus(Resource):

    @sandbox_api.doc(security='apikey')
    @sandbox_api.expect(sandbox_collection_api_requestpament)
    def get(self):
        """ get payment request status sandbox collection. """
        try:
            parser = reqparse.RequestParser(bundle_errors=True)
            parser.add_argument("access_token", type=str, required=True)
            parser.add_argument("environment", type=str, required=True)
            parser.add_argument("x_reference_id", type=str, required=True)
            args = parser.parse_args()
            payment = Payment.request_payment_status(args)
            return payment
        except Exception as e:
            return {"message": str(e)}, 500
