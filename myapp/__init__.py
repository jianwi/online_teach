from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    # flask app 实例化
    app = Flask(__name__,
                static_folder="static",
                static_url_path="/static",
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

    from myapp.front.view import front
    app.register_blueprint(front, url_prefix="/front")

    return app