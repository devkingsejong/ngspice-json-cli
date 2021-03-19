from flask import Flask
from flask_restful import Api
import ngspicejson.config as config


app = Flask(__name__)
app.config.from_object(config)

api_root = Api(app, catch_all_404s=True)
from .api import *
