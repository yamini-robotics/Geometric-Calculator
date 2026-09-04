class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


    def area(self):
        return 3.141592653589793 * (self.radius ** 2)


    def circumference(self):
        return 2 * 3.141592653589793 * self.radius