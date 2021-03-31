from flask_restful import Resource
from .. import api_root
from flask import request
from ...service.business.simulate_ngspice import simulate
import tempfile
import os


@api_root.resource('/run')
class Run(Resource):

    def post(self):
        file = request.files['file']

        new_file, filename = tempfile.mkstemp()
        os.write(new_file, file.read())
        result = simulate("", filename)
        os.close(new_file)
        return result
