
import math

class Point (object):

    def __init__ (self, x = 0, y = 0):

        self.x = x

        self.y = y

    def __str__ (self):

        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __eq__ (self, other):

        tol = 1 * 10 ** -6

        if(abs(self.x - other.x) < tol and abs(self.y - other.y) < tol):

            return True

        else:

            return False

    def dist (self, other):

        dist_points = math.hypot((self.x - other.x), (self.y - other.y))

        return dist_points
        

class Circle (object):

    def __init__ (self, x = 0, y = 0, radius = 1):

        self.center = Point(x, y)

        self.radius = radius

    def __str__ (self):

        return 'Center: ' + str(self.center) + ' radius: ' + str(self.radius)

    def circumference (self):

        return 2 * math.pi * self.radius

    def area (self):

        return math.pi * self.radius ** 2

    def point_inside (self, p):

        if (self.center.dist(p) < self.radius):

            return True

        else:

            return False

    def circle_inside (self, other):

        dist_centers = self.center.dist(other.center)

        if (dist_centers + other.radius < self.radius):

            return True

        else:

            return False

    def circle_outside (self, other):

        dist_centers = self.center.dist(other.center)

        if (dist_centers - other.radius > self.radius):

            return True

        else:

            return False

    def circle_intersect (self, other):

        return (not self.circle_inside(other) and \
                not self.circle_outside(other))
    
