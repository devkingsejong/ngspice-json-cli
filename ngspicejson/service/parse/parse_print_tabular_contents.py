from .abstract_parse import AbstractParse
import re
from ..tool.marshal import simple_keyvalues_marshal, dynamic_keyvalues_marshal, KEY_TITLE, VALUE_TITLE


class ParsePrintTabularContents(AbstractParse):
    def _detect_target(self):
        return re.findall(r"(Index.*time.*\n----.*\n(\d{1,}[	 ].*[	 ].*[	 ]?.*\n){1,})", self.input)

    def _parse(self, target_list):
        result_of_all_prints = []
        count_for_bulk_data_list = 1
        for t in target_list:  # List of Index time branch ------ 0 1e-08 3.2 .......
            target = t[0]  # ('Index time branch ------ 0 1e-08 3.2 ......., 0 1e-08 3.2)
            target = target.split("\n")

            """
            00 = {str} 'Index   time            v1#branch       '
            01 = {str} '--------------------------------------------------------------------------------'
            02 = {str} '0\t0.000000e+00\t0.000000e+00\t'
            """

            first_data_line = target[2].split()[0]

            if first_data_line[0] == "0":  # Init mode
                temp = simple_keyvalues_marshal("print_#{0}".format(count_for_bulk_data_list), [])

                list_of_data = target[0].split()[1:]
                for data in list_of_data:
                    temp[VALUE_TITLE].append(dynamic_keyvalues_marshal("data_name", data.strip(), []))

                result_of_all_prints.append(temp)
                count_for_bulk_data_list+=1

            bulk_data = target[2:]
            for data_line in bulk_data:
                data_line = data_line.split()  # TODO: 스페이스도 지원
                data_line = data_line[1:]

                for idx, data in enumerate(data_line):
                    if data == "":
                        continue
                    result_of_all_prints[-1][VALUE_TITLE][idx][VALUE_TITLE].append(data.strip())

        return result_of_all_prints

    def _get_title(self):
        return "TABULARCONTENTS"
