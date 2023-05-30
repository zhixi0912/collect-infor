"""
ORM映射数据库操作：
1：flask db init
2：flask db migrate
3：flask db upgrade
"""


class Config(object):
    JSON_AS_ASCII = False
    SECRET_KEY = "qwerasdfzxcv"
    HOSTNAME = "127.0.0.1"
    # HOSTNAME = "10.0.12.8"
    DATABASE_PORT = "3306"
    DATABASE = "collect_info"  # 数据库名
    USERNAME = "root"
    # PASSWORD = "QWERasdf1234"
    PASSWORD = "root1234"
    DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOSTNAME, DATABASE_PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI

    # redis  启动redis-server
    REDIS_PORT = 6379
    # REDIS_PASSWORD = 'QWERasdf1234'
    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_COOKIE_HTTPONLY = False  # 使cookie可以被访问
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒  24小时
    TOKEN_EXP = 1   # token有效时间（单位：天）


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}