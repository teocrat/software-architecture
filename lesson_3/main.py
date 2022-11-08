from rectangle import Rectangle
from triangle import Triangle
from square import Square
from circle import Circle

figures = [Rectangle(12, 23), Triangle(24, 23, 21), Square(2)]

for i in figures:
    print(f'Area {i.area():.2f}\nPerimeter {i.perimeter():.2f}')
f = Circle(10)
print(f'Area {f.area():.2f}\nCircumference {f.circumference():.2f}')
