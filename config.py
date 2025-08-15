class BaseConfig:
    SECRET_KEY = '123456789'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/forum?charset=utf8mb4"

    MAIL_SERVER = "smtp.qq.com"
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_USERNAME = "2368996924@qq.com"
    MAIL_PASSWORD = "huxyljfxunyuebic"
    MAIL_DEFAULT_SENDER = "2368996924@qq.com"


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
