from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api_root = Api(app, catch_all_404s=True)
from .api import *
