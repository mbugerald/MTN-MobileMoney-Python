import base64
import uuid

import requests

from config import GLOBALS


class Users:

    # Create api user for collection if the user does not exist.
    @classmethod
    def create_collection_users(cls, data) -> (int, str, list):
        try:
            # request headers.
            x_reference_id = str(uuid.uuid4())
            headers = {
                "Content-Type": "application/json",
                "Ocp-Apim-Subscription-Key": GLOBALS.MOMO_API_KEY_COLLECTION,
                "X-Reference-Id": x_reference_id
            }
            # request body
            body = {
                "providerCallbackHost": data.provider_callback_host or GLOBALS.MOMO_USER_REDIRECT_URI
            }
            req = requests.post(
                GLOBALS.MOMO_CREATE_COLLECTION_USER,
                headers=headers,
                json=body
            )
            if req.status_code != 201:
                return req.json(), req.status_code
            return {
                       "message": "Successfully created",
                       "x-reference-id": x_reference_id
                   }, req.status_code
        except Exception as e:
            return {"message": str(e)}, 500

    # Obtain api key
    @classmethod
    def obtain_api_key(cls, data):
        try:
            # request headers.
            headers = {
                "Content-Type": "application/json",
                "Ocp-Apim-Subscription-Key": GLOBALS.MOMO_API_KEY_COLLECTION,
            }
            # Send request
            req = requests.post(
                GLOBALS.MOMO_CREATE_COLLECTION_USER + f"/{data.x_reference_id}/apikey",
                headers=headers
            )
            # Obtain authorization Bearer key
            oauth = cls.obtain_api_token(data.x_reference_id + ":" + req.json()["apiKey"])
            return {
                       "apiKey": req.json()["apiKey"],
                       "authorization": oauth
                   }, req.status_code
        except Exception as e:
            return {"message": str(e)}, 500

    @classmethod
    def obtain_api_token(cls, message) -> (str, object, int):
        try:
            # Encode X-reference-id and apikey to obtain Bearer base64 encoding.
            message = message.encode("ascii")
            base64_bytes = base64.b64encode(message)
            base64_message = base64_bytes.decode('ascii')
            # Use the authorization obtained to generate token

            # headers
            headers = {
                "Ocp-Apim-Subscription-Key": GLOBALS.MOMO_API_KEY_COLLECTION,
                "Authorization": "Basic " + base64_message,
            }
            req = requests.post(
                GLOBALS.MOMO_CREATE_COLLECTION_TOKEN,
                headers=headers
            )
            if req.status_code != 200:
                return req.json(), req.status_code
            return req.json(), 200
        except Exception as e:
            return {"message": str(e)}, 500
