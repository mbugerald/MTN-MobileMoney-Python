import os
# from schedules import SCHEDULES_CELERY_BEAT
# from queues import QUEUES_CELERY, QUEUES_CELERY_ROUTES


class Base:

    DEBUG = True
    APP_SETUP = True
    PORT = 5000
    HOST = "0.0.0.0"
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    MAIL_SERVER = "smtp-relay.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    MAIL_PASSWORD = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "simple"  # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 300
    SECURITY_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


class Development(Base):
    PORT = 5000
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_NATIVE_UNICODE = True
    SQLALCHEMY_DATABASE_URI = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    # Flask swagger config
    SWAGGER_BASEPATH = '/api/v1/'
    SWAGGER_UI_JSONEDITOR = True
    CORS_HEADERS = 'Content-Type'
    BUNDLE_ERRORS = True
    SWAGGER_UI_OPERATION_ID = True
    SWAGGER_UI_REQUEST_DURATION = True
    WHOOSH_BASE = 'whoosh'

    # Flask compress
    COMPRESS_MIMETYPES = [
        'application/json',
        'application/javascript'
    ]
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500
    COMPRESS_REGISTER = True

    # Amazon S3
    AWS_ACCESS_KEY_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    AWS_SECRET_ACCESS_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    S3_BUCKET_NAME = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    @staticmethod
    def init_app(app):
        pass

class PreProd(Base):
    pass


# Object production handler
class Production(Base):
    pass


# Object test handler
class Test(Base):
    pass


# Config arguments
config = {
    'DEVELOPMENT': Development,
    'DEFAULT': Development
}


class GLOBALS:
    ENV = "DEVELOPMENT"
    SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    MOMO_API_KEY_COLLECTION = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    MOMO_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    MOMO_UUID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    MOMO_URI_SANDBOX = "https://sandbox.momodeveloper.mtn.com"
    MOMO_URI = "https://sandbox.momodeveloper.mtn.com"
    MOMO_URI_REQUEST_PAYMENT = f"{MOMO_URI_SANDBOX}/collection/v1_0/requesttopay"
    MOMO_TEST_NUMBERS = "46733123453"
    MOMO_HEADER = {
        'Authorization': '',
        'X-Callback-Url': '',
        'X-Reference-Id': '',
        'X-Target-Environment': '',
        'Ocp-Apim-Subscription-Key': f'{MOMO_API_KEY}',
    }
    MOMO_CREATE_COLLECTION_USER = f"{MOMO_URI_SANDBOX}/v1_0/apiuser"
    MOMO_CREATE_COLLECTION_TOKEN = f"{MOMO_URI_SANDBOX}/collection/token/"
    MOMO_USER_REDIRECT_URI = "https://callback-will-not-work-in-the-sandbox.com"
