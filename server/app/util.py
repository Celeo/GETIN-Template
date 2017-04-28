from functools import wraps

from flask import request
from flask_restful import abort
from jose import jwt

from .shared import config
from .models import User


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['Authorization']
            token_data = jwt.decode(token, config['SECRET_KEY'])
            user = User.query.filter_by(name=token_data['name']).first()
            if user:
                return f(*args, **kwargs)
            abort(401)
        except:
            abort(401)
    return wrapper
