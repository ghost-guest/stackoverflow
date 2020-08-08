from flask import Flask, render_template
from flask_login import LoginManager
from .handlers import blueprint_list
from flask_migrate import Migrate
from .configs import configs
from .models import db, User


def register_extionsions(app):
    for bp in blueprint_list:
        app.register_blueprint(bp)
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'front.index'
    login_manager.refresh_view = 'front.index'

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)


def create_app(config):
    app = Flask(__name__)
    # app.config 是一个类字典对象，它有一个 from_object 方法
    # 此方法可以将类的实例作为参数，从中读取配置项
    # 注意读取的配置项为全大写的类属性
    # 所以 configs.py 文件中的类属性名应为全大写，用下划线连接
    app.config.from_object(configs.get(config))
    # 该行代码的作用是初始化应用 app
    # 这样 app 的配置项 SQLALCHEMY_DATABASE_URI 就会起到作用了
    register_extionsions(app)
    return app
