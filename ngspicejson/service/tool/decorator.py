from .ngspice_tool import check_ngspice_is_installed
from .exception import GlobalException


def needs_ngspice(f):
    def wrap(*args, **kwargs):
        a, b = check_ngspice_is_installed()
        if a:
            return f(*args, **kwargs)
        else:
            return str(GlobalException("NgspiceNotFoundException",
                                    "You should install NGSPICE. If your NGSPICE is alrealdy installed,"
                                    " check the alias settings."))

    return wrap
