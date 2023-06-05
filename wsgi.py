import os

from werkzeug.security import generate_password_hash

from blog.app import create_app
from blog.models.database import db

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
