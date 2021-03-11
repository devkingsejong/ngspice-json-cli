from .abstract_parse import AbstractParse
from ..tool.marshal import simple_keyvalues_marshal, dynamic_keyvalues_marshal
import re


class ParseInitialTransientSolution(AbstractParse):
    def _detect_target(self):
        return re.findall(r"(Initial Transient Solution\n"
                          r"--------------------------\n\n"
                          r"Node.*Voltage\n----.*-------\n([a-z].*\n){1,})", self.input)

    def _parse(self, target_list):

        result_of_all_prints = []
        target_list = target_list[0][0].split("\n")[5:]
        """
                [('Initial Transient Solution\n--------------------------\n\n
                Node                                   Voltage\n----                                   -------\n
                int                                          0\nin                                           0\n
                out                                          0\nv1#branch                                    0\n',
                'v1#branch                                    0\n')]
        """

        for target in target_list:
            """
            ['int                                          0', 'in                                           0',
             'out                                          0', 'v1#branch                                    0', '']
            """
            if target.strip() == '':
                continue
            list_of_model = ' '.join(target.split()).split()

            temp = dynamic_keyvalues_marshal("node", list_of_model[0],
                                             simple_keyvalues_marshal("Voltage", list_of_model[1]))
            result_of_all_prints.append(temp)
        return result_of_all_prints

    def _get_title(self):
        return "INITIAL_TRANSIENT_SOLUTION"
