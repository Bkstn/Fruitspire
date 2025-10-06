from flask import Flask
from config import Config
from db.models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    return {"status": "ok", "message": "Food Notifier API running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables based on your models
    app.run(debug=True)
