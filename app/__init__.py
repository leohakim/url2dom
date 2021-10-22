from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # UTF-8

from app import views