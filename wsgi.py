import os

from blog.models.database import db
from blog.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )


@app.cli.command("create-admin")
def create_users():
    """
    Run in your terminal:
    flask create-admin
    > created admin: <User #1 'admin'>
    """
    from blog.models import User
    admin = User(username="admin", email="admin@admin.ru", is_staff=True)
    admin.password = os.environ.get("ADMIN_PASSWORD") or "admin"
    db.session.add(admin)
    db.session.commit()

    print("done! created admin:", admin)


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
