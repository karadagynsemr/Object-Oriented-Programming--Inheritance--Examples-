import math
from cs1graphics import *

class RegularPolygon(Polygon):
    def __init__(self, center=Point(0,0)):
        super().__init__()
        self._num_sides = 4
        self._side_length = 4
        self._center = center
        self._generate_points()

    def _generate_points(self):
        angle = 360 / self._num_sides
        for i in range(self._num_sides):
            x = self._center.getX() + self._side_length * math.cos(math.radians(i * angle))
            y = self._center.getY() + self._side_length * math.sin(math.radians(i * angle))
            self.addPoint(Point(x, y))
