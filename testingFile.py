from flask import request, Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)   

@app.route('/')
def index():
    return "THIS IS AN INDEX PAGE"
@app.route('/hello')
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {escape(name)}!"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))