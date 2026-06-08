from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    date_registered = db.Column(db.DateTime, default=datetime.utcnow)
    fridges = db.relationship("Fridge", back_populates="user", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_registered": self.date_registered.isoformat() if self.date_registered else None,
            "fridges": [fridge.to_dict(shallow=True) for fridge in self.fridges],
        }


class Fridge(db.Model):
    __tablename__ = "fridges"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    user = db.relationship("User", back_populates="fridges")
    items = db.relationship("FoodItem", back_populates="fridge", cascade="all, delete-orphan")

    def to_dict(self, shallow=False):
        data = {
            "id": self.id,
            "name": self.name,
            "date_created": self.date_created.isoformat() if self.date_created else None,
        }
        if not shallow:
            data["items"] = [item.to_dict() for item in self.items]
        return data


class FoodItem(db.Model):
    __tablename__ = "food_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_expire = db.Column(db.DateTime, nullable=True)
    fridge_id = db.Column(db.Integer, db.ForeignKey("fridges.id"), nullable=False)
    fridge = db.relationship("Fridge", back_populates="items")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date_added": self.date_added.isoformat() if self.date_added else None,
            "date_expire": self.date_expire.isoformat() if self.date_expire else None,
            "fridge_id": self.fridge_id,
        }
