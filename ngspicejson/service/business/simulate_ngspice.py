import time

from ..tool.ngspice_tool import ngspice_with_command
from ..parse import INJECT_TARGETS
from ..tool.exception import GlobalException
from ..business.ngspice_error_message import parse_ngspice_error_messages
from ..business.debug_message import make_debug_message


def simulate(command, file, tag=None, real=False, debug=False):
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

        return temp
    except GlobalException as e:
        return str(e)
    except Exception as e:
        temp_exception = GlobalException('SomethingBadException',
                                         'A fatal error that can not be processed by the program has occurred.',
                                         )
        return str(temp_exception)
