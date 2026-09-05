class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, p):

        dx = p.x - self.x
        dy = p.y - self.y

        return (dx ** 2 + dy ** 2) ** 0.5

