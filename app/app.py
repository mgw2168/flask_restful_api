from flask import Flask


def register_bp(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_bp(app)

    return app
