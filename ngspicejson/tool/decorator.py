from .ngspice_tool import check_ngspice_is_installed
from .exception import global_exception


def needs_ngspice(f):
    def wrap(*args, **kwargs):
        a, b = check_ngspice_is_installed()
        if a:
            return f(*args, **kwargs)
        else:
            return global_exception("NGSPICE NOT FOUND EXCEPTION",
                                    "You should install NGSPICE. If your NGSPICE is alrealdy installed,"
                                    " check the alias settings.")

    return wrap
