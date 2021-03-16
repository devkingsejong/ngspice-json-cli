import fire
from service.tool.decorator import needs_ngspice
from service.tool.ngspice_tool import ngspice_with_command, ngspice
import json
from service.parse.parse_model_list import ParseModelList
from service.parse.parse_initial_transient_solution import ParseInitialTransientSolution
from service.parse.parse_print_tabular_contents import ParsePrintTabularContents
from service.parse.parse_ngspice_version import ParseNgspiceVersion
from service.business.preordered_ngspice_command import get_ngspice_verison
from service.parse import inject_target


class NGSPICEJsonCli:

    @needs_ngspice
    def version(self):
        return json.dumps({'ngspice': get_ngspice_verison(), 'ngspice-json-cli': '0.0.1'})

    @needs_ngspice
    def run(self, command, file):

        get_all_device_information = ngspice_with_command(command, file)

        temp = []
        for target in inject_target:
            try:
                parse = target(get_all_device_information)
                result_of_all_prints = parse.dict()
                temp.append(result_of_all_prints)
            except:
                pass
        return json.dumps(temp)
        #
        # m = ParseModelList(get_all_device_information)
        # result_of_all_prints = m.dict()
        # return json.dumps(result_of_all_prints)
    #
    # @needs_ngspice
    # def run2(self, command, file):
    #
    #     get_all_device_information = ngspice_with_command(command, file)
    #
    #     m = ParseInitialTransientSolution(get_all_device_information)
    #     result_of_all_prints = m.dict()
    #     return json.dumps(result_of_all_prints)
    #
    # @needs_ngspice
    # def run3(self, command, file):
    #
    #     get_all_device_information = ngspice_with_command(command, file)
    #     m = ParsePrintTabularContents(get_all_device_information)
    #     result_of_all_prints = m.dict()
    #     return json.dumps(result_of_all_prints)
    #
    # @needs_ngspice
    # def run4(self, command, file):
    #
    #     get_all_device_information = ngspice("-v")
    #     m = ParseNgspiceVersion(get_all_device_information)
    #     result_of_all_prints = m.dict()
    #     return json.dumps(result_of_all_prints)


if __name__ == '__main__':
    fire.Fire(NGSPICEJsonCli)
