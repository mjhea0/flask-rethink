from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_precious"

from app import views
