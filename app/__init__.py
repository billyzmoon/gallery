from flask import Flask

app = Flask(__name__, static_url_path='/')

from app.api import api

app.register_blueprint(api)
