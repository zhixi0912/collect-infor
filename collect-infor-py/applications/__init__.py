from flask import Flask, request, g
from applications.extensions import db
from applications import api_1_0
from applications.configs.config import config_map, Config
from flask_cors import CORS
import jwt
from jwt import exceptions
import redis

# 创建redis连接对象  控制台输入redis-server启动本地redis
redis_store = None


def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 （"develop",  "product"）
    :return:
    """
    app = Flask(__name__)
    config_type = config_map.get(config_name)
    app.config.from_object(config_type)
    db.init_app(app)
    CORS(app)   # 处理跨域
    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_type.HOSTNAME, port=config_type.REDIS_PORT)
    # 部署线上时打开
    # redis_store = redis.StrictRedis(host=config_type.HOSTNAME, port=config_type.REDIS_PORT, password=config_type.PASSWORD)
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")



    @app.before_request
    def jwt_authentication():
        """
        1.获取请求头Authorization中的token
        2.判断是否以 Bearer开头
        3.使用jwt模块进行校验
        4.判断校验结果,成功就提取token中的载荷信息,赋值给g对象保存
        """
        auth = request.headers.get('Authorization')
        if auth and auth.startswith('Bearer '):  # Bearer是Authorization的类型声明，会放在token的头部，所以要用auth[7:]截去留下真正的token
            "提取token 0-6 被Bearer和空格占用 取下标7以后的所有字符 token=Bearer ***..."
            token = auth[7:]
            "校验token"
            g.username = None
            try:
                "判断token的校验结果"
                payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
                "获取载荷中的信息赋值给g对象"
                g.username = payload.get('username')
            except exceptions.ExpiredSignatureError:    # 'token已失效'
                g.username = 1
            except jwt.DecodeError:                     # 'token认证失败'
                g.username = 2
            except jwt.InvalidTokenError:               # '非法的token'
                g.username = 3

    return app


