from rectangle import Rectangle


class Square(Rectangle):
    def area(self):
        return self.height ** 2

    def perimeter(self):
        return self.height * 4

    def __init__(self, height):
        super().__init__(height, width=height)
        self.height = height

