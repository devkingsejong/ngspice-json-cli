from .abstract_parse import AbstractParse
import re


class ModelListParse(AbstractParse):
    def _detect_target(self):
        return re.findall(r"\s?[A-Z].*:\s[A-Z].*\n[A-Za-z\s0-9-]{1,}\n.{1,}.*\n.{1,}", self.input)

    def _parse(self, target_list):

        result_of_all_prints = []
        for source in target_list:

            source_lines = source.split("\n")

            title_line = source_lines[0].strip()
            title_line = title_line.split(":")
            title = title_line[0]
            title_description = title_line[1].strip()

            temp = {"title": title, "description": title_description, "contents": []}

            del source_lines[0]
            list_of_device = ' '.join(source_lines[0].split()).split()[1:]
            for t in list_of_device:
                temp['contents'].append({"model": t, "vals": []})

            del source_lines[0]

            for t in source_lines:
                list_of_model = ' '.join(t.split()).split()
                if len(list_of_model)-1 == len(list_of_device):  # 신규 등록 모드
                    line = list_of_model
                    temp_title = line[0]
                    for idx, tt in enumerate(line[1:]):
                        temp['contents'][idx]['vals'].append({"title": temp_title, "value": [tt]})

                else:
                    line = list_of_model
                    for idx, tt in enumerate(line[0:]):
                        temp['contents'][idx]['vals'][-1]['value'].append(tt)

            result_of_all_prints.append(temp)

        return result_of_all_prints

    def _get_title(self):
        return "NODEMODEL"
