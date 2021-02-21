import requests

from config import GLOBALS


class Payment:

    @classmethod
    def request_collection_payment(cls, data) -> (list, str, int):

        # headers
        headers = {
            "Authorization": f"Bearer {data.access_token}",
            "X-Reference-Id": f"{data.x_reference_id}",
            "Ocp-Apim-Subscription-Key": f"{GLOBALS.MOMO_API_KEY_COLLECTION}",
            "X-Target-Environment": f"{data.environment}",
            "Content-Type": "application/json"
        }

        # Body
        body = {
            "amount": data.amount,
            "currency": data.currency,
            "externalId": data.x_reference_id,
            "payer": {
                "partyIdType": "MSISDN",
                "partyId": f"{data.phone_number}"
            },
            "payerMessage": data.payer_message,
            "payeeNote": data.payer_note
        }

        try:
            r = requests.post(
                url=GLOBALS.MOMO_URI_REQUEST_PAYMENT,
                json=body,
                headers=headers
            )
            if r.status_code != 202:
                return r.json(), r.status_code
            return {
                "message": "Payment request successfully sent to the client.",
                "intent": "Awaiting client mobile transfer validation"
                   }, r.status_code
        except Exception as e:
            return {"message": str(e)}, 500

    @classmethod
    def request_payment_status(cls, data) -> (str, list, int):
        try:

            # headers
            headers = {
                "Authorization": f"Bearer {data.access_token}",
                "Ocp-Apim-Subscription-Key": f"{GLOBALS.MOMO_API_KEY_COLLECTION}",
                "X-Target-Environment": f"{data.environment}",
                "Content-Type": "application/json"
            }

            print(data.x_reference_id)
            r = requests.get(
                    url=f"{GLOBALS.MOMO_URI_REQUEST_PAYMENT}/{data.x_reference_id}",
                    headers=headers
            )
            if r.status_code != 200:
                return r.json(), r.status_code
            return r.json(), r.status_code
        except Exception as e:
            return {"message": str(e)}, 500
