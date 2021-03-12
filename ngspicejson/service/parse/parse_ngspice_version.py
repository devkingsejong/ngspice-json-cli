from .abstract_parse import AbstractParse
from ..tool.marshal import simple_keyvalues_marshal
import re


class ParseNgspiceVersion(AbstractParse):
    def _detect_target(self):
        return re.findall(r"(\*\*\*\*\*\*\n.*\n.*\n.*\n.*\n.*\n.*\n\*\*\*\*\*\*)|"
                          r"(.*ngspice revision [0-9]{1,}.*\n.*\n.*\n\n.*\n.*)", self.input)

    def _parse(self, target_list):

        result_of_all_prints = []
        for target in target_list:  # [('ngspice..', ''), ('', 'ngspice..')]
            target = [x for x in target if x][0]
            version = re.findall(r"(ngspice revision [0-9]{1,}|ngspice-[0-9]{1,})", target)[0]  # ['ngspice-32']
            version = version.replace('-', " ")  # ngspice-32 or ngspice revision 27
            version = version.split(" ")
            result_of_all_prints.append(simple_keyvalues_marshal("version", version[-1]))

        return result_of_all_prints

    def _get_title(self):
        return "NGSPICE_VERSION"
