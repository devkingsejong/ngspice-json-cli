import unittest
import json
from ...parse.model_list_parse import ModelListParse


# python -m ngspicejson.service.test.command.show_all
class MyTestCase(unittest.TestCase):
    maxDiff = None

    def test_맥OS_10_15_7_ngspice34_빌드버전_출력을_잘_파싱하는지(self):

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
        model_list_parse = ModelListParse(cli_input)
        result_of_all_prints = model_list_parse.dict()
        correct_output = """
        {"type": "NODEMODEL", "contents": [{"title": "Capacitor", "description": "Fixed capacitor", "contents": [{"model": "c2", "vals": [{"title": "model", "value": ["C"]}, {"title": "capacitance", "value": ["1e-07"]}, {"title": "dtemp", "value": ["0"]}, {"title": "bv_max", "value": ["0"]}]}, {"model": "c1", "vals": [{"title": "model", "value": ["C"]}, {"title": "capacitance", "value": ["1e-06"]}, {"title": "dtemp", "value": ["0"]}, {"title": "bv_max", "value": ["0"]}]}]}, {"title": "Resistor", "description": "Simple linear resistor", "contents": [{"model": "r2", "vals": [{"title": "model", "value": ["R"]}, {"title": "resistance", "value": ["1000"]}, {"title": "ac", "value": ["1000"]}, {"title": "dtemp", "value": ["0"]}, {"title": "bv_max", "value": ["0"]}, {"title": "noisy", "value": ["0"]}]}, {"model": "r1", "vals": [{"title": "model", "value": ["R"]}, {"title": "resistance", "value": ["10000"]}, {"title": "ac", "value": ["10000"]}, {"title": "dtemp", "value": ["0"]}, {"title": "bv_max", "value": ["0"]}, {"title": "noisy", "value": ["0"]}]}]}, {"title": "Vsource", "description": "Independent voltage source", "contents": [{"model": "v1", "vals": [{"title": "dc", "value": ["0"]}, {"title": "acmag", "value": ["0"]}, {"title": "pulse", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "sin", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "exp", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "pwl", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "sffm", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "am", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "trnoise", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}, {"title": "trrandom", "value": ["0", "5", "1e-06", "1e-06", "1e-06", "1", "1"]}]}]}]}
        """

        correct_output = json.loads(correct_output)
        del result_of_all_prints['real']  # 실제 출력 값을 표시하는 부분 삭제

        self.assertEqual(result_of_all_prints, correct_output)


if __name__ == '__main__':
    unittest.main()
