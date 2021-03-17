from abc import ABCMeta, abstractmethod
from ..tool.marshal import global_marshal


class AbstractParse(metaclass=ABCMeta):

    def __init__(self, input, real=False):
        self.input = input
        self.real = real

    def dict(self):
        target_list = self._detect_target()
        real = self.input if self.real is True else ""
        try:
            parse = self._parse(target_list)
        except:
            parse = []
        return global_marshal(self._get_title(), parse, real)

    @abstractmethod
    def _detect_target(self):
        pass

    @abstractmethod
    def _parse(self, target_list):
        pass

    @abstractmethod
    def _get_title(self):
        pass
