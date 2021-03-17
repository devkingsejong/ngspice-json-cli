import unittest
import json
from ngspicejson.service.parse.parse_ngspice_version import ParseNgspiceVersion


# python -m ngspicejson.test.command.ngspice_version
class TestParseNgspiceVersion(unittest.TestCase):
    maxDiff = None

    def test_맥OS_10_15_7_ngspice34_버전_출력을_잘_파싱하는지(self):

        cli_input = """
******
** ngspice-34 : Circuit level simulation program
** The U. C. Berkeley CAD Group
** Copyright 1985-1994, Regents of the University of California.
** Copyright 2001-2020, The ngspice team.
** Please get your ngspice manual from http://ngspice.sourceforge.net/docs.html
** Please file your bug-reports at http://ngspice.sourceforge.net/bugrep.html
******
"""
        model_list_parse = ParseNgspiceVersion(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """{"type": "NGSPICE_VERSION", "contents": [{"key": "version", "values": ["34"]}]}"""
        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제
        self.assertEqual(result_of_all_prints, correct_output)

    def test_Ubuntu_18_04_5_ngspice27_버전_출력을_잘_파싱하는지(self):

        cli_input = """
ngspice compiled from ngspice revision 27
Written originally by Berkeley University
Currently maintained by the NGSpice Project

Copyright (C) 1985-1996,  The Regents of the University of California
Copyright (C) 1999-2011,  The NGSpice Project
"""
        model_list_parse = ParseNgspiceVersion(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """{"type": "NGSPICE_VERSION", "contents": [{"key": "version", "values": ["27"]}]}"""
        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제

        self.assertEqual(result_of_all_prints, correct_output)


if __name__ == '__main__':
    unittest.main()
