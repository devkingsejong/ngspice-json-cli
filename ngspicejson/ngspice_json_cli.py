import fire
import time
import json

from service.tool.decorator import needs_ngspice
from service.tool.ngspice_tool import ngspice_with_command
from service.business.preordered_ngspice_command import get_ngspice_verison
from service.parse import INJECT_TARGETS
from service.tool.exception import GlobalException
from service.business.ngspice_error_message import parse_ngspice_error_messages
from service.business.debug_message import make_debug_message


class NGSPICEJsonCli:

    @needs_ngspice
    def version(self):
        return json.dumps({'ngspice': get_ngspice_verison(), 'ngspice-json-cli': '0.0.1'})

    @needs_ngspice
    def run(self, command, file, tag=None, real=False, debug=False):
        start = time.time()
        try:
            get_all_device_information, err_output, real_command = ngspice_with_command(command, file)

            temp = []
            temp.append(parse_ngspice_error_messages(err_output))  # Error Message always placed head of list.

            for target in INJECT_TARGETS:
                try:
                    parse = target(get_all_device_information, real)
                    result_of_all_prints = parse.dict()
                    temp.append(result_of_all_prints)
                except:
                    pass
            if tag is not None or debug is True:  # Debug Message always placed tail of list.
                temp.append(make_debug_message(tag, time.time()-start, ' '.join(real_command)))

            return json.dumps(temp)
        except GlobalException as e:
            return str(e)
        except Exception as e:
            temp_exception = GlobalException('SomethingBadException',
                                             'A fatal error that can not be processed by the program has occurred.',
                                             )
            return str(temp_exception)


if __name__ == '__main__':
    fire.Fire(NGSPICEJsonCli)
