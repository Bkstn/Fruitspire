from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask
from config import Config


db = SQLAlchemy()



class FoodItem(db.Model):
    __tablename__ = "food_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    user_chat_id = db.Column(db.String(50), nullable=False)
    notified = db.Column(db.Boolean, default=False)

    def is_expiring_soon(self, days=3):
        delta = (self.expiration_date - datetime.now().date()).days
        return delta <= days
