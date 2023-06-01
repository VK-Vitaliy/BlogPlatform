from flask import Flask, render_template
from flask_migrate import Migrate
from blog.auth.views import auth_app, login_manager
from blog.users.views import users_app
from blog.articles.views import articles_app
from blog.models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("blog.config")
    register_blueprints(app)
    register_extensions(app)


    @app.route("/")
    def index():
        return render_template("index.html")

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)
    app.register_blueprint(articles_app)
    app.register_blueprint(auth_app)


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app, db)


