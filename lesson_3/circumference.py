import abc


class Circumference(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def circumference(self):
        pass
