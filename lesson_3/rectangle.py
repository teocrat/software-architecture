from shape import Shape


class Rectangle(Shape):
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.height + self.width) * 2

    def __init__(self, height, width):
        self.height = height
        self.width = width

        if self.height <= 0 or self.width <= 0:
            raise ValueError('Rectangle does not exist')
