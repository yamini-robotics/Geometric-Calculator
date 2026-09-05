PI = 3.141592653589793


class Sphere:

    def __init__(self, x, y, z, radius):

        if radius <= 0:
            raise ValueError("Radius must be positive")

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

    def surface_area(self):
        return 4 * PI * (self.radius ** 2)

    def volume(self):
        return (4 / 3) * PI * (self.radius ** 3)


class Cylinder:

    def __init__(self, x, y, z, radius, height):

        if radius <= 0 or height <= 0:
            raise ValueError("Radius and height must be positive")

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * PI * self.radius * (self.radius + self.height)

    def volume(self):
        return PI * (self.radius ** 2) * self.height


class Cuboid:

    def __init__(self, x, y, z, length, width, height):

        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Length, width and height must be positive")

        self.x = x
        self.y = y
        self.z = z
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (
            self.length * self.width
            + self.length * self.height
            + self.width * self.height
        )

    def volume(self):
        return self.length * self.width * self.height