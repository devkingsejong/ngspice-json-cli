from flask_restful import Resource
from .. import api_root
from flask import request
from ...service.business.simulate_ngspice import simulate


@api_root.resource('/run')
class Run(Resource):

    def post(self):
        file = request.files['file']
        return simulate("", file.filename)
