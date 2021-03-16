from ..tool.marshal import global_marshal


def parse_ngspice_error_messages(error_output, real=False):
    split_error_output = error_output.split('\n')
    temp = []
    for error in split_error_output:
        error = error.strip()
        if error == "":
            continue
        temp.append(error)

    real = error_output if real is True else ""
    return global_marshal("NGSPICE_CLI_ERROR", temp, real)
