import fire
import json

from .config import VERSION
from .service.tool.decorator import needs_ngspice
from .service.business.preordered_ngspice_command import get_ngspice_verison
from .service.business.simulate_ngspice import simulate
import ngspicejson
import subprocess


class NGSPICEJsonCli:

    @needs_ngspice
    def version(self):
        return json.dumps({'ngspice': get_ngspice_verison(), 'ngspice-json-cli': VERSION})

    @needs_ngspice
    def server(self, host='0.0.0.0', port='32541', venv=None):
        http_socket = "{0}:{1}".format(host, port)
        ini_file_path = ngspicejson.__file__.split('ngspicejson/__init__.py')[0]+'uwsgi.ini'

        if venv is None:
            return_code = subprocess.call("uwsgi --http {0} {1}".format(http_socket, ini_file_path), shell=True)
        else:
            return_code = subprocess.call("uwsgi --http {0} --venv {1} {2}".format(http_socket, venv, ini_file_path),
                                          shell=True)

    @needs_ngspice
    def run(self, command, file, tag=None, real=False, debug=False):
        return json.dumps(simulate(command, file, tag, real, debug))


if __name__ == '__main__':
    fire.Fire(NGSPICEJsonCli)
