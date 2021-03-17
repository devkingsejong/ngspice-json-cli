import unittest
import json
from ngspicejson.service.parse.parse_model_list import ParseModelList


# python -m ngspicejson.test.command.show_all
class TestParseShowAllCommand(unittest.TestCase):
    maxDiff = None

    def test_맥OS_10_15_7_ngspice34_전체노드_출력을_잘_파싱하는지(self):

        cli_input = """
No compatibility mode selected!


Circuit: dual rc ladder

ngspice 97 -> show all
 Capacitor: Fixed capacitor
     device                    c2                    c1
      model                     C                     C
capacitance                 1e-07                 1e-06
      dtemp                     0                     0
     bv_max                     0                     0

 Resistor: Simple linear resistor
     device                    r2                    r1
      model                     R                     R
 resistance                  1000                 10000
         ac                  1000                 10000
      dtemp                     0                     0
     bv_max                     0                     0
      noisy                     0                     0

 Vsource: Independent voltage source
     device                    v1
         dc                     0
      acmag                     0
      pulse                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
        sin                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
        exp                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
        pwl                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
       sffm                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
         am                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
    trnoise                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
   trrandom                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1

ngspice 98 -> ngspice-34 done
"""
        model_list_parse = ParseModelList(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """
{"type":"NODEMODEL","contents":[{"title":"Capacitor","description":"Fixed capacitor","contents":[{"model":"c2","values":[{"key":"model","values":["C"]},{"key":"capacitance","values":["1e-07"]},{"key":"dtemp","values":["0"]},{"key":"bv_max","values":["0"]}]},{"model":"c1","values":[{"key":"model","values":["C"]},{"key":"capacitance","values":["1e-06"]},{"key":"dtemp","values":["0"]},{"key":"bv_max","values":["0"]}]}]},{"title":"Resistor","description":"Simple linear resistor","contents":[{"model":"r2","values":[{"key":"model","values":["R"]},{"key":"resistance","values":["1000"]},{"key":"ac","values":["1000"]},{"key":"dtemp","values":["0"]},{"key":"bv_max","values":["0"]},{"key":"noisy","values":["0"]}]},{"model":"r1","values":[{"key":"model","values":["R"]},{"key":"resistance","values":["10000"]},{"key":"ac","values":["10000"]},{"key":"dtemp","values":["0"]},{"key":"bv_max","values":["0"]},{"key":"noisy","values":["0"]}]}]},{"title":"Vsource","description":"Independent voltage source","contents":[{"model":"v1","values":[{"key":"dc","values":["0"]},{"key":"acmag","values":["0"]},{"key":"pulse","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"sin","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"exp","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"pwl","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"sffm","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"am","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"trnoise","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"trrandom","values":["0","5","1e-06","1e-06","1e-06","1","1"]}]}]}]}        """

        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제

        self.assertEqual(result_of_all_prints, correct_output)

    def test_Ubuntu_18_04_5_ngspice27_전체노드_출력을_잘_파싱하는지(self):

        cli_input = """
Capacitor: Fixed capacitor
     device                    c2                    c1
      model                     C                     C
capacitance                 1e-07                 1e-06
      dtemp                     0                     0
     bv_max                 1e+99                 1e+99
          i           4.88031e-07           4.83598e-06
          p           2.41393e-06           2.39224e-05

 Resistor: Simple linear resistor
     device                    r2                    r1
      model                     R                     R
 resistance                  1000                 10000
         ac                  1000                 10000
      dtemp                     0                     0
     bv_max                 1e+99                 1e+99
      noisy                     1                     1
          i          -4.88031e-07          -5.32401e-06
          p           2.38174e-10           2.83451e-07

 Vsource: Independent voltage source
     device                    v1
         dc                     0
      acmag                     0
      pulse                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
        sin                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
        exp                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
        pwl                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
       sffm                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
         am                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
    trnoise                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
   trrandom                     0
                                5
                            1e-06
                            1e-06
                            1e-06
                                1
                                1
          i          -5.32401e-06
          p           2.66201e-05
"""
        model_list_parse = ParseModelList(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """
{"type":"NODEMODEL","contents":[{"title":"Resistor","description":"Simple linear resistor","contents":[{"model":"r2","values":[{"key":"model","values":["R"]},{"key":"resistance","values":["1000"]},{"key":"ac","values":["1000"]},{"key":"dtemp","values":["0"]},{"key":"bv_max","values":["1e+99"]},{"key":"noisy","values":["1"]},{"key":"i","values":["-4.88031e-07"]},{"key":"p","values":["2.38174e-10"]}]},{"model":"r1","values":[{"key":"model","values":["R"]},{"key":"resistance","values":["10000"]},{"key":"ac","values":["10000"]},{"key":"dtemp","values":["0"]},{"key":"bv_max","values":["1e+99"]},{"key":"noisy","values":["1"]},{"key":"i","values":["-5.32401e-06"]},{"key":"p","values":["2.83451e-07"]}]}]},{"title":"Vsource","description":"Independent voltage source","contents":[{"model":"v1","values":[{"key":"dc","values":["0"]},{"key":"acmag","values":["0"]},{"key":"pulse","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"sin","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"exp","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"pwl","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"sffm","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"am","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"trnoise","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"trrandom","values":["0","5","1e-06","1e-06","1e-06","1","1"]},{"key":"i","values":["-5.32401e-06"]},{"key":"p","values":["2.66201e-05"]}]}]}]}
        """
        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제

        self.assertEqual(result_of_all_prints, correct_output)


if __name__ == '__main__':
    unittest.main()
