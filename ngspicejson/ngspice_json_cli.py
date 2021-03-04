import fire
from tool.decorator import needs_ngspice


class NGSPICEJsonCli:

    @needs_ngspice
    def test(self):
        return "hi roo"


if __name__ == '__main__':
  fire.Fire(NGSPICEJsonCli)