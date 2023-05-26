from flask import Flask, render_template

from blog.auth.views import auth_app, login_manager
from blog.users.views import users_app
from blog.articles.views import articles_app
from blog.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    app.config["SECRET_KEY"] = "!-3e@ck&icam8&-qc8fm+vk7mz=lj%)li@va+e7-7_@@qvdria"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    login_manager.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app)





