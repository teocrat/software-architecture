import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass
