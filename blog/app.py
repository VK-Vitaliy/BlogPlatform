from flask import Flask, render_template

from blog.users.views import users_app


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def index():
        return render_template("index.html")
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(users_app)


