from .abstract_parse import AbstractParse
import re
from ..tool.marshal import simple_keyvalues_marshal, dynamic_keyvalues_marshal, KEY_TITLE, VALUE_TITLE


class ParseModelList(AbstractParse):
    def _detect_target(self):
        return re.findall(r"\s?[A-Z].*:\s[A-Z].*\n[A-Za-z\s0-9\+\-\.\_]{1,}\n", self.input)

    def _parse(self, target_list):

        result_of_all_prints = []
        for source in target_list:

            source_lines = source.split("\n")

            title_line = source_lines[0].strip()
            title_line = title_line.split(":")
            if len(title_line) != 2:
                continue
            title = title_line[0]
            title_description = title_line[1].strip()

            temp = {"title": title, "description": title_description, "contents": []}

            del source_lines[0]
            list_of_device = ' '.join(source_lines[0].split()).split()[1:]
            for t in list_of_device:
                temp['contents'].append(dynamic_keyvalues_marshal("model", t, []))

            del source_lines[0]

            for t in source_lines:
                list_of_model = ' '.join(t.split()).split()
                if len(list_of_model)-1 == len(list_of_device):  # 신규 등록 모드
                    line = list_of_model
                    temp_title = line[0]
                    for idx, tt in enumerate(line[1:]):

                        temp['contents'][idx][VALUE_TITLE].append(simple_keyvalues_marshal(temp_title, [tt]))

                else:
                    line = list_of_model
                    for idx, tt in enumerate(line[0:]):
                        temp['contents'][idx][VALUE_TITLE][-1][VALUE_TITLE].append(tt)

            result_of_all_prints.append(temp)

        return result_of_all_prints

    def _get_title(self):
        return "NODEMODEL"
