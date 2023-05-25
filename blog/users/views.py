from flask import Blueprint, render_template

users_app = Blueprint(
    name="users_app",
    import_name=__name__,
    static_folder="../static",
    url_prefix="/users",
)

USERS = {
    1: "James",
    2: "Brian",
    3: "Peter",
}


@users_app.route("/")
def user_list():
    return render_template("users/list.html", users=USERS)
