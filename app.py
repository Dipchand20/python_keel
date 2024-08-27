# app.py
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! dipchand yadav !!1"

@app.route("/fancy")
def hello_world_fancy():
    greetings = """
    <html>
    <body>

    <h1>Greetings!</h1>
    <p>Hello, world!</p>

    </body>
    </html>
    """
    return greetings
