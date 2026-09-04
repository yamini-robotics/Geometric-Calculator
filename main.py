from point import Point
from line import Line
from circle import Circle
from rectangle import Rectangle


shape = input("Enter shape (point, line, circle, rectangle): ")

if shape == "point":

    x = float(input("Enter x: "))
    y = float(input("Enter y: "))

    p1 = Point(x, y)

    print("Point:", p1.x, p1.y)


elif shape == "line":

    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))

    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)

    l1 = Line(p1, p2)

    print("Length:", l1.length())


elif shape == "circle":

    x = float(input("Enter center x: "))
    y = float(input("Enter center y: "))

    radius = float(input("Enter radius: "))

    center = Point(x, y)

    c1 = Circle(center, radius)

    print("Area:", c1.area())
    print("Circumference:", c1.circumference())


elif shape == "rectangle":

    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))

    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))

    x4 = float(input("Enter x4: "))
    y4 = float(input("Enter y4: "))

    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    p4 = Point(x4, y4)

    length = p1.distance(p2)
    width = p1.distance(p4)

    area = length * width
    perimeter = 2 * (length + width)

    print("Area:", area)
    print("Perimeter:", perimeter)


else:
    print("Invalid shape")