class BaseConfig:
    SECRET_KEY = '123456789'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/forum?charset=utf8mb4"

class TestingConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass


