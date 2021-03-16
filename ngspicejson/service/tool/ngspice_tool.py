import subprocess
from .exception import GlobalException


def check_ngspice_is_installed():
    try:

        result = ngspice("-v")
        return True, result
    except FileNotFoundError:
        return False, ""


def ngspice(*arg):
    result = subprocess.check_output(["ngspice", *arg])
    return result.decode('utf-8')


def ngspice_with_command(command, file, *arg):
    try:
        # raise FileNotFoundError
        pipe = subprocess.check_output(["printf", "{0}".format(command)])
        result = subprocess.run(["ngspice", "-p", "-n", "{0}".format(file)], input=pipe, capture_output=True)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8'), result.args
    except (subprocess.CalledProcessError, subprocess.SubprocessError, FileNotFoundError) as e:
        raise GlobalException("NgspiceCLIiError", "Error occurred during run Ngspice cli.")
