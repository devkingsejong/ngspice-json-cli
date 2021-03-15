from .abstract_parse import AbstractParse
from ..tool.marshal import simple_keyvalues_marshal
import re


class ParseSpecificPrint(AbstractParse):
    def _detect_target(self):
        return re.findall("^(([0-9a-zA-Z\#\[\]\(\)]{1,} = [0-9a-zA-Z\+\-\.]{1,}\n){1,})",
                          self.input, flags=re.MULTILINE)

    def _parse(self, target_list):

        result_of_all_prints = []
        for idx, target in enumerate(target_list):  # [('ngspice..', ''), ('', 'ngspice..')]
            temp = simple_keyvalues_marshal("print_#{0}".format(idx), [])
            target = target[0]
            target = target.split("\n")
            for line in target:
                if line == "":
                    continue
                line = line.split("=")
                temp['values'].append(simple_keyvalues_marshal(line[0], line[1]))

            result_of_all_prints.append(temp)

        return result_of_all_prints

    def _get_title(self):
        return "SPECIFIC_PRINT"
