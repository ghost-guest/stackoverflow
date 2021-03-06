import os

class BaseConfig:
    """
    配置基类
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'haha'

class DevConfig(BaseConfig):
    """
    开发环境配置类
    """
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    uri = 'mysql://root:{}@127.0.0.1:3306/qa?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = uri.format(os.environ.get('MYSQL_PWD'))
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/qa?charset=utf8'


class ProConfig(BaseConfig):
    pass


configs = {'dev': DevConfig, 'pro': ProConfig}