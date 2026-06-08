from flask import Flask, jsonify
from config import Config
from db.models import db, FoodItem

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def home():
    return jsonify({"message": "Fruitspire API is running"})


@app.route("/fruits")
def get_fruits():
    fruits = FoodItem.query.all()
    return jsonify([fruit.to_dict() for fruit in fruits])


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
