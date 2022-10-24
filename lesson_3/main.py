from rectangle import Rectangle
from triangle import Triangle
from square import Square
from circle import Circle

figures = [Rectangle(12, 23), Triangle(24, 23, 21), Square(23), Circle(24)]

for i in figures:
    print(f'Area {i.area():.2f}\nPerimeter {i.perimeter():.2f}')


