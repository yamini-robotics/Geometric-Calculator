from point import Point
from line import Line
from circle import Circle

p1 = Point(12.62, 14.74)
p2 = Point(20.24, 30.59)

print(p1.distance(p2))

l1 = Line(p1, p2)

print(l1.length())

c1 = Circle(p1, 5)

print(c1.area())
print(c1.circumference())