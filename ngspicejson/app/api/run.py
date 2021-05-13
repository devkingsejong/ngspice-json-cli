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
        extra_figure = request.form.get('figure')
        new_file, filename = tempfile.mkstemp()
        os.write(new_file, file.read())

        result = simulate("show all", filename)

        if extra_figure is not None:
            avail_node_list = list(map(lambda x: x['node'], result[1]['contents']))
            user_node = extra_figure.split(",")
            if set(user_node).issubset(avail_node_list):
                result = simulate("print {0}".format(' '.join(user_node)), filename)

        os.close(new_file)
        return result
