import abc
from math import pi


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


class CounterPerimeter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def perimeter(self):
        pass


class CounterCircumference(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def circumference(self):
        pass


class Rectangle(Shape, CounterPerimeter):

    def __init__(self, height, width):
        self.height = height
        self.width = width

        if self.height <= 0 and self.width <= 0:
            raise ValueError('Rectangle does not exist')

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.height + self.width) * 2


class Square(Shape, CounterPerimeter):

    def __init__(self, height):
        self.height = height

        if self.height <= 0:
            raise ValueError('Square does not exist')

    def area(self):
        return self.height ** 2

    def perimeter(self):
        return self.height * 4


class Triangle(Shape, CounterPerimeter):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (self.c + self.b) < self.a:
            raise ValueError('Triangle does not exist')

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


class Circle(Shape, CounterCircumference):
    def __init__(self, radius):
        self.radius = radius

        if self.radius <= 0:
            raise ValueError('Circle does not exist')

    def area(self):
        return pi * self.radius ** 2

    def circumference(self):
        return 2 * pi * self.radius


if __name__ == '__main__':
    a = Square(3.4)
    print('Square:')
    print(f'Area {a.area(): .2f}')
    print(f'Perimeter {a.perimeter(): .2f}')
    print('-' * 10)
    b = Rectangle(5.6, 12.9)
    print('Rectangle:')
    print(f'Area {b.area(): .2f}')
    print(f'Perimeter {b.perimeter(): .2f}')
    print('-' * 10)
    c = Triangle(12, 23, 23.6)
    print('Triangle:')
    print(f'Area {c.area(): .2f}')
    print(f'Perimeter {c.perimeter(): .2f}')
    print('-' * 10)
    d = Circle(3.5)
    print('Circle:')
    print(f'Area {d.area(): .2f}')
    print(f'Circumference {d.circumference(): .2f}')
