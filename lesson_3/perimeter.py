import abc


class Perimeter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def perimeter(self):
        pass
