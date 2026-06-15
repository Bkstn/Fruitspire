from flask import Flask, jsonify, request
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

#this allows to add data using PowerShell 
@app.route("/fruits", methods = ["POST"])
def add_fruit():
    data = request.get_json()
    new_fruit = FoodItem(name = data["name"], date_expire = data.get("date_expire"), fridge_id = data["fridge_id"]
                         )
    db.session.add(new_fruit)
    db.session.commit()

    return jsonify(new_fruit.to_dict()), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
