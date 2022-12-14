from shape import Shape
from math import pi
from circumference import Circumference


class Circle(Shape, Circumference):

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius

    def __init__(self, radius):
        self.radius = radius

        if self.radius <= 0:
            raise ValueError('Circle does not exist')
