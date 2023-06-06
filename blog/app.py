from flask import Flask, render_template
from flask_migrate import Migrate

from blog.views.auth import auth_app, login_manager
from blog.models.database import db
from blog.security import flask_bcrypt
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.authors import authors_app

from blog.admin import admin


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
    app.register_blueprint(authors_app)


def register_extensions(app: Flask):
    db.init_app(app)
    login_manager.init_app(app)
    flask_bcrypt.init_app(app)
    migrate = Migrate(app, db, compare_type=True)
    migrate.init_app(app, db)
    admin.init_app(app)
