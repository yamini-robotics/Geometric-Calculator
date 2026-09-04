class Line:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    def length(self):

        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y

        return (dx ** 2 + dy ** 2) ** 0.5

        