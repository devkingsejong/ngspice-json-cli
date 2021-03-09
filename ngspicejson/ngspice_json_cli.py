import fire
from service.tool.decorator import needs_ngspice
from service.tool.ngspice_tool import ngspice_with_command
import json
from service.parse.model_list_parse import ModelListParse

class NGSPICEJsonCli:

    @needs_ngspice
    def run(self, command, file):

        get_all_device_information = ngspice_with_command(command, file)

        m = ModelListParse(get_all_device_information)
        result_of_all_prints = m.dict()
        return json.dumps(result_of_all_prints)


if __name__ == '__main__':
  fire.Fire(NGSPICEJsonCli)