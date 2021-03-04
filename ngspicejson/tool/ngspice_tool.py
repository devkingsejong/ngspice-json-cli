import subprocess


def check_ngspice_is_installed():
    try:

        result = ngspice("-v")
        return True, result
    except FileNotFoundError:
        return False, ""


def ngspice(*arg):
    result = subprocess.check_output(["ngspice", *arg])
    return result
