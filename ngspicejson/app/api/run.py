from flask_restful import Resource
from .. import api_root
from ...service.business.preordered_ngspice_command import get_ngspice_verison
from flask import request
import os, tempfile
import json
from ngspicejson.service.business.simulate_ngspice import simulate


@api_root.resource('/run')
class Run(Resource):

    def post(self):
        file = request.files['file']
        print(file.filename)
        return simulate("", file.filename)
