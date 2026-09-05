from point import Point
from line import Line
from circle import Circle
from rectangle import Rectangle


def point_to_point(p1, p2):
    return p1.distance(p2)


def point_to_line(point, line):
    x1 = line.p1.x
    y1 = line.p1.y

    x2 = line.p2.x
    y2 = line.p2.y

    dx = x2 - x1
    dy = y2 - y1

    if dx == 0 and dy == 0:
        return point.distance(line.p1)

    t = ((point.x - x1) * dx + (point.y - y1) * dy) / (dx ** 2 + dy ** 2)

    if t < 0:
        t = 0
    elif t > 1:
        t = 1

    closest_x = x1 + t * dx
    closest_y = y1 + t * dy

    closest_point = Point(closest_x, closest_y)

    return point.distance(closest_point)


def point_to_circle(point, circle):
    center_distance = point.distance(circle.center)

    distance = center_distance - circle.radius

    if distance < 0:
        return 0

    return distance


def point_to_rectangle(point, rectangle):
    x1 = min(rectangle.p1.x, rectangle.p2.x)
    x2 = max(rectangle.p1.x, rectangle.p2.x)

    y1 = min(rectangle.p1.y, rectangle.p2.y)
    y2 = max(rectangle.p1.y, rectangle.p2.y)

    if x1 <= point.x <= x2 and y1 <= point.y <= y2:
        return 0

    if point.x < x1:
        dx = x1 - point.x
    elif point.x > x2:
        dx = point.x - x2
    else:
        dx = 0

    if point.y < y1:
        dy = y1 - point.y
    elif point.y > y2:
        dy = point.y - y2
    else:
        dy = 0

    return (dx ** 2 + dy ** 2) ** 0.5


def line_to_line(line1, line2):
    d1 = point_to_line(line1.p1, line2)
    d2 = point_to_line(line1.p2, line2)
    d3 = point_to_line(line2.p1, line1)
    d4 = point_to_line(line2.p2, line1)

    return min(d1, d2, d3, d4)


def line_to_circle(line, circle):
    center_distance = point_to_line(circle.center, line)

    distance = center_distance - circle.radius

    if distance < 0:
        return 0

    return distance


def line_to_rectangle(line, rectangle):
    d1 = point_to_rectangle(line.p1, rectangle)
    d2 = point_to_rectangle(line.p2, rectangle)

    return min(d1, d2)


def circle_to_circle(circle1, circle2):
    center_distance = circle1.center.distance(circle2.center)

    distance = center_distance - circle1.radius - circle2.radius

    if distance < 0:
        return 0

    return distance


def circle_to_rectangle(circle, rectangle):
    center_distance = point_to_rectangle(circle.center, rectangle)

    distance = center_distance - circle.radius

    if distance < 0:
        return 0

    return distance


def rectangle_to_rectangle(rectangle1, rectangle2):
    x1_min = min(rectangle1.p1.x, rectangle1.p2.x)
    x1_max = max(rectangle1.p1.x, rectangle1.p2.x)

    y1_min = min(rectangle1.p1.y, rectangle1.p2.y)
    y1_max = max(rectangle1.p1.y, rectangle1.p2.y)

    x2_min = min(rectangle2.p1.x, rectangle2.p2.x)
    x2_max = max(rectangle2.p1.x, rectangle2.p2.x)

    y2_min = min(rectangle2.p1.y, rectangle2.p2.y)
    y2_max = max(rectangle2.p1.y, rectangle2.p2.y)

    if x1_max < x2_min:
        dx = x2_min - x1_max
    elif x2_max < x1_min:
        dx = x1_min - x2_max
    else:
        dx = 0

    if y1_max < y2_min:
        dy = y2_min - y1_max
    elif y2_max < y1_min:
        dy = y1_min - y2_max
    else:
        dy = 0

    return (dx ** 2 + dy ** 2) ** 0.5


def distance(shape1, shape2):

    if isinstance(shape1, Point) and isinstance(shape2, Point):
        return point_to_point(shape1, shape2)

    elif isinstance(shape1, Point) and isinstance(shape2, Line):
        return point_to_line(shape1, shape2)

    elif isinstance(shape1, Line) and isinstance(shape2, Point):
        return point_to_line(shape2, shape1)

    elif isinstance(shape1, Point) and isinstance(shape2, Circle):
        return point_to_circle(shape1, shape2)

    elif isinstance(shape1, Circle) and isinstance(shape2, Point):
        return point_to_circle(shape2, shape1)

    elif isinstance(shape1, Point) and isinstance(shape2, Rectangle):
        return point_to_rectangle(shape1, shape2)

    elif isinstance(shape1, Rectangle) and isinstance(shape2, Point):
        return point_to_rectangle(shape2, shape1)

    elif isinstance(shape1, Line) and isinstance(shape2, Line):
        return line_to_line(shape1, shape2)

    elif isinstance(shape1, Line) and isinstance(shape2, Circle):
        return line_to_circle(shape1, shape2)

    elif isinstance(shape1, Circle) and isinstance(shape2, Line):
        return line_to_circle(shape2, shape1)

    elif isinstance(shape1, Line) and isinstance(shape2, Rectangle):
        return line_to_rectangle(shape1, shape2)

    elif isinstance(shape1, Rectangle) and isinstance(shape2, Line):
        return line_to_rectangle(shape2, shape1)

    elif isinstance(shape1, Circle) and isinstance(shape2, Circle):
        return circle_to_circle(shape1, shape2)

    elif isinstance(shape1, Circle) and isinstance(shape2, Rectangle):
        return circle_to_rectangle(shape1, shape2)

    elif isinstance(shape1, Rectangle) and isinstance(shape2, Circle):
        return circle_to_rectangle(shape2, shape1)

    elif isinstance(shape1, Rectangle) and isinstance(shape2, Rectangle):
        return rectangle_to_rectangle(shape1, shape2)

    else:
        raise ValueError("Distance between these shapes is not supported")