# Library imports
from functools import wraps
from flask import request
import jwt
import random, string
from app import Config
from app.database import (Users)


# Token inspector
from config import GLOBALS


def token_required(f):
    @wraps(f)
    def decorated(self, *args, **kwargs):
        try:
            token = None
            if 'x-access-token' in request.headers or request.args.get('x-access-token', default=None):
                if 'x-access-token' in request.headers:
                    token = request.headers['x-access-token']
                else:
                    token = request.args.get('x-access-token', default=None)
                if not token:
                    return {'message': 'Permission denied token is required!'}, 401
                try:
                    # Decode the generated token on access login.
                    data = jwt.decode(token, GLOBALS.SECRET_KEY)
                    current_user = Users.query.filter_by(public_id=data["public_id"]).first()
                except:
                    return {'message': 'Token is invalid!'}, 401
                if current_user is None:
                    return {'message': 'Token is invalid!'}, 401
                return f(self, current_user, *args, **kwargs)
            if not token:
                return {'message': 'Permission denied token is required!'}, 401
        except Exception as e:
            #apm.capture_exception()
            return {'message': 'Permission denied token is required!' + str(e)}, 401

    return decorated


# token handler for sockets
def token_socketio(token):
    try:
        if token is None:
            return {"message": "No token provided."}, 412
            # Decode the generated token on access login.
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            current_user = Users.query.filter_by(
                public_id=data["public_id"]).first()
        except:
            return {"message": "Token is invalid!"}, 401
        return str(current_user.public_id)
    except Exception:
        # apm.capture_exception()
        return {"message": "Server Error!"}, 500


def generate_random_password():
    try:
        length = 14
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        rnd = random.SystemRandom()
        return ''.join(rnd.choice(chars) for i in range(length))
    except Exception as e:
        #apm.capture_exception()
        return {"message": "Server Error!"}, 500

