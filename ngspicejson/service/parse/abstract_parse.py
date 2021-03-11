from abc import ABCMeta, abstractmethod
from ..tool.marshal import global_marshal


class AbstractParse(metaclass=ABCMeta):

    def __init__(self, input):
        self.input = input

    def dict(self):
        target_list = self._detect_target()
        return global_marshal(self._get_title(), self._parse(target_list), self.input)

    @abstractmethod
    def _detect_target(self):
        pass

    @abstractmethod
    def _parse(self, target_list):
        pass

    @abstractmethod
    def _get_title(self):
        pass
