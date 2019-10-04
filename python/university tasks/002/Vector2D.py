import math


class Vector2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "<%s, %s>" % (self.x, self.y)

    def __add__(self, v):
        return Vector2D(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vector2D(self.x - v.x, self.y - v.y)

    def __mul__(self, d):
        if isinstance(d, (int, float)):
            return Vector2D(self.x * d, self.y * d)
        if isinstance(d, Vector2D):
            return d.x * self.x + d.y * self.y
    def __eq__(self, v):
        return self.x == v.x and self.y == v.y

    def __abs__(self):
        return int(math.sqrt(self.x) + math.sqrt(self.y))

    def __len__(self):
        return abs(self)

v1 = Vector2D(2,1)
v2 = Vector2D(9,4)
v3 = Vector2D()
