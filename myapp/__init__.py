from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # flask app 实例化
    app = Flask(__name__,
                static_folder="../fronted",
                static_url_path="/html",
                )
    # 加载配置
    app.config.from_object("config.Config")
    # 初始化db
    db.init_app(app)

    # 路由
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    # 蓝图注册
    # 前台用户登录
    from myapp.front.auth import front_auth
    app.register_blueprint(front_auth, url_prefix="/front_auth/")

    # 前台 Blueprint
    from myapp.front.view import front
    app.register_blueprint(front, url_prefix="/front")

    # 后台验证
    from myapp.admin.auth import admin_auth
    app.register_blueprint(admin_auth, url_prefix="/admin_auth/")

    # 后台Blueprint
    from myapp.admin.view import admin
    app.register_blueprint(admin, url_prefix="/admin/")

    # 文件上传与下载
    from myapp.api.file import file
    app.register_blueprint(file, url_prefix="/file/")


    # api
    from myapp.api.api import api
    app.register_blueprint(api, url_prefix="/api/")
    return app
