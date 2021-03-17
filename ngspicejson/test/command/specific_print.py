import unittest
import json
from ngspicejson.service.parse.parse_specific_print import ParseSpecificPrint


# python -m ngspicejson.test.command.specific_print
class TestParseSpecificPrint(unittest.TestCase):
    maxDiff = None

    def test_맥OS_10_15_7_ngspice34_특정값_출력을_잘_파싱하는지(self):

        cli_input = """
******
** ngspice-34 : Circuit level simulation program
** The U. C. Berkeley CAD Group
** Copyright 1985-1994, Regents of the University of California.
** Copyright 2001-2020, The ngspice team.
** Please get your ngspice manual from http://ngspice.sourceforge.net/docs.html
** Please file your bug-reports at http://ngspice.sourceforge.net/bugrep.html
******
ngspice 244 -> source printone.cir

No compatibility mode selected!


Circuit: v1 1 0 dc=1v

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000

Using transient initial conditions

No. of Data Rows : 111
Can't open viewport for graphics.
time[k] = 1.000000e-03
v(2)[k] = 0.000000e+00
ngspice 245 -> 
"""
        model_list_parse = ParseSpecificPrint(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """
        {"type": "SPECIFIC_PRINT", "contents": [{"key": "print_#0", "values": [{"key": "time[k] ", "values": [" 1.000000e-03"]}, {"key": "v(2)[k] ", "values": [" 0.000000e+00"]}]}]}
        """
        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제
        self.assertEqual(result_of_all_prints, correct_output)

    def test_Ubuntu_18_04_5_ngspice27_특정값_출력을_잘_파싱하는지(self):

        cli_input = """******
** ngspice-27 : Circuit level simulation program
** The U. C. Berkeley CAD Group
** Copyright 1985-1994, Regents of the University of California.
** Please get your ngspice manual from http://ngspice.sourceforge.net/docs.html
** Please file your bug-reports at http://ngspice.sourceforge.net/bugrep.html
** Creation Date: Tue Dec 26 17:10:20 UTC 2017
******
ERROR: (external)  no graphics interface;
 please check if X-server is running,
 or ngspice is compiled properly (see INSTALL)
ngspice 1 -> source printone.cir

Circuit: v1 1 0 dc=1v

Doing analysis at TEMP = 27.000000 and TNOM = 27.000000


Initial Transient Solution
--------------------------

Node                                   Voltage
----                                   -------
1                                            0
2                                            0



No. of Data Rows : 112
Can't open viewport for graphics.
time[k] = 1.000000e-03
v(2)[k] = 0.000000e+00
ngspice 1 ->"""
        model_list_parse = ParseSpecificPrint(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """
        {"type": "SPECIFIC_PRINT", "contents": [{"key": "print_#0", "values": [{"key": "time[k] ", "values": [" 1.000000e-03"]}, {"key": "v(2)[k] ", "values": [" 0.000000e+00"]}]}]}
        """
        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제
        self.assertEqual(result_of_all_prints, correct_output)


if __name__ == '__main__':
    unittest.main()
