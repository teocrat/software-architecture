from shape import Shape


class Triangle(Shape):

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (self.c + self.b) < self.a:
            raise ValueError('Triangle does not exist')
