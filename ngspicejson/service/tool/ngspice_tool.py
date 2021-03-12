import subprocess
import os


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
    result = os.popen('printf "{0}" | ngspice -p -n {1}'.format(command, file)).read()

    return result
