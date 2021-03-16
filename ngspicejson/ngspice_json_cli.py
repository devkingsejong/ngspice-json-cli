import fire
from service.tool.decorator import needs_ngspice
from service.tool.ngspice_tool import ngspice_with_command
import json
from service.business.preordered_ngspice_command import get_ngspice_verison
from service.parse import inject_target
from service.tool.exception import GlobalException
from service.business.ngspice_error_message import parse_ngspice_error_messages
from service.business.debug_message import make_debug_message


class NGSPICEJsonCli:

    @needs_ngspice
    def version(self):
        return json.dumps({'ngspice': get_ngspice_verison(), 'ngspice-json-cli': '0.0.1'})

    @needs_ngspice
    def run(self, command, file, tag=None, real=False):
        try:
            get_all_device_information, err_output = ngspice_with_command(command, file)

            temp = []
            temp.append(parse_ngspice_error_messages(err_output))  # Error Message always placed head of list.

            for target in inject_target:
                try:
                    parse = target(get_all_device_information, real)
                    result_of_all_prints = parse.dict()
                    temp.append(result_of_all_prints)
                except:
                    pass
            if tag is not None:  # Debug Message always placed tail of list.
                temp.append(make_debug_message(tag))

            return json.dumps(temp)
        except GlobalException as e:
            return str(e)


if __name__ == '__main__':
    fire.Fire(NGSPICEJsonCli)
