from flask import jsonify, g, current_app, request
from applications.utils.response_code import RET, error_map
from applications.configs.config import Config
from functools import wraps
import jwt
from jwt import exceptions
import datetime


headers = {
    'typ': 'jwt',
    'alg': 'HS256'
}


def create_token(username, user_id):
    payload = {
        'username': username,
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=Config.TOKEN_EXP)
    }
    result = jwt.encode(
        # encoding='utf-8',
        payload=payload,
        key=Config.SECRET_KEY,
        algorithm='HS256',
        headers=headers
    )
    return result.encode('utf-8').decode('utf-8')


def verify_jwt(token, secret=None):
    """
    校验token
    :param token:   jwt
    :param secret: Config.SECRET_KEY
    :return:    dict: payload
    """
    if not secret:
        secret = current_app.config('JWT_SECRET')
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        return payload
    except exceptions.ExpiredSignatureError:    # token失效
        return 1
    except jwt.DecodeError:     # token认证失败
        return 2
    except jwt.InvalidTokenError:   # token非法
        return 3


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            if g.username ==1:
                return {'code': 4001, 'message': 'token已失效'}, 401
            elif g.username == 2:
                return {'code': 4001, 'message': 'token认证失败'}, 401
            elif g.username == 3:
                return {'code': 4001, 'message': '非法的token'}, 401
            else:
                return func(*args, **kwargs)
        except BaseException as e:
            return {'code': 4001, 'message': '请先登录'}, 401
    return wrapper



