from flask_restful import Resource
from .. import api_root, app
from ...service.business.preordered_ngspice_command import get_ngspice_verison


@api_root.resource('/version')
class Version(Resource):

    def get(self):
        return {
            'ngspice': get_ngspice_verison(),
            'ngspice-json-cli': app.config["VERSION"],
            'message': "Welcome To ngspice-json-cli server!"
        }
