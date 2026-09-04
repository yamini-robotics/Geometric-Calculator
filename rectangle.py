class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        length = abs(self.p2.x - self.p1.x)
        width = abs(self.p2.y - self.p1.y)



        return length * width

    def perimeter(self):
        length = abs(self.p2.x - self.p1.x)
        width = abs(self.p2.y - self.p1.y)

        return 2 * (length + width)