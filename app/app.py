from flask import Flask


def register_bp(app):
    from app.api.v1.book import book
    from app.api.v1.user import user

    app.register_blueprint(user)
    app.register_blueprint(book)

def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_bp(app)

    return app
