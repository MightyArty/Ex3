from math import sqrt


class Location:

    """Constructor"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, point):
        return sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2) + pow(self.z - point.z, 2))
