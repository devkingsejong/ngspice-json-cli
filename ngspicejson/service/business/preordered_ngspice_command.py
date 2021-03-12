from ..tool.ngspice_tool import ngspice
from ..parse.parse_ngspice_version import ParseNgspiceVersion
from ..tool.marshal import VALUE_TITLE


def get_ngspice_verison():
    try:
        get_all_device_information = ngspice("-v")
        m = ParseNgspiceVersion(get_all_device_information)
        result_of_all_prints = m.dict()
        version = result_of_all_prints['contents'][0][VALUE_TITLE][0]
        return version
    except:
        return -1
