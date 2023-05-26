from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"User #{self.id} {self.username}"
