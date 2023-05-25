from flask import Blueprint, render_template

articles_app = Blueprint(
    name="articles_app",
    import_name=__name__,
    static_folder="../static",
    url_prefix="/articles",
)

ARTICLES = ["Flask", "Django", "JSON:API"]


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)
