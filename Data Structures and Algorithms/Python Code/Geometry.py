#  File: Geometry.py

#  Description: The purpose of this program is to begin developing
#               object oriented programming by creating different
#               classes create gemoetric objects (Point, Sphere, Cube
#               Cylinder)

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/17/2021

#  Date Last Modified: 06/21/2021

import math

class Point (object):
    
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
      
        self.x = float(x)

        self.y = float(y)

        self.z = float(z)

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):

        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
    def distance (self, other):

        import math

        self.dist =  math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2) + ((self.z - other.z) ** 2))

        return self.dist

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
    def __eq__ (self, other):

        tol = 1.0 * (10 ** -6)

        return((abs(self.x - other.x) < tol) and \
               (abs(self.y - other.y) < tol) and \
               (abs(self.z - other.z) < tol))

class Sphere (object):
    
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):

        self.x = float(x)

        self.y = float(y)

        self.z = float(z)

        self.center = Point(self.x, self.y, self.z)

        self.radius = float(radius)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):

        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + '), Radius: ' + str(self.radius)

  # compute surface area of Sphere
  # returns a floating point number
    def area (self):

        import math

        self.area = math.pi * 4 * (self.radius ** 2)

        return self.area

  # compute volume of a Sphere
  # returns a floating point number
    def volume (self):

        import math

        self.volume = math.pi * (4/3) * (self.radius ** 3)

        return self.volume

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
    def is_inside_point (self, p):

        # Checks each individual dimension (x, y, z)

        if(self.center.distance(p) < self.radius):

            return True
        
        else:

            return False
                                                                        
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, other):

        dist_centers = self.center.distance(other.center)

        if((dist_centers + other.radius) < self.radius):

            return True

        else:

            return False

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
    def is_inside_cube (self, a_cube):

        corner_1 = Point(a_cube.x + a_cube.side / 2, \
                         a_cube.y + a_cube.side / 2, \
                         a_cube.z + a_cube.side / 2)

        corner_2 = Point(a_cube.x + a_cube.side / 2, \
                         a_cube.y + a_cube.side / 2, \
                         a_cube.z - a_cube.side / 2)

        corner_3 = Point(a_cube.x + a_cube.side / 2, \
                         a_cube.y - a_cube.side / 2, \
                         a_cube.z + a_cube.side / 2)

        corner_4 = Point(a_cube.x + a_cube.side / 2, \
                         a_cube.y - a_cube.side / 2, \
                         a_cube.z - a_cube.side / 2)

        corner_5 = Point(a_cube.x - a_cube.side / 2, \
                         a_cube.y + a_cube.side / 2, \
                         a_cube.z + a_cube.side / 2)

        corner_6 = Point(a_cube.x - a_cube.side / 2, \
                         a_cube.y + a_cube.side / 2, \
                         a_cube.z - a_cube.side / 2)

        corner_7 = Point(a_cube.x - a_cube.side / 2, \
                         a_cube.y - a_cube.side / 2, \
                         a_cube.z + a_cube.side / 2)

        corner_8 = Point(a_cube.x - a_cube.side / 2, \
                         a_cube.y - a_cube.side / 2, \
                         a_cube.z - a_cube.side / 2)

        dist_centers = self.center.distance(a_cube.center)

        if(dist_centers + a_cube.side / 2 < self.radius and \
           self.center.distance(corner_1) < self.radius and \
           self.center.distance(corner_2) < self.radius and \
           self.center.distance(corner_3) < self.radius and \
           self.center.distance(corner_4) < self.radius and \
           self.center.distance(corner_5) < self.radius and \
           self.center.distance(corner_6) < self.radius and \
           self.center.distance(corner_7) < self.radius and \
           self.center.distance(corner_8) < self.radius):

            return True

        else:

            return False
        
  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
    def is_inside_cyl (self, a_cyl):

        dist_centers = self.center.distance(a_cyl.center)

        dist_center_to_height = math.hypot(dist_centers, a_cyl.height / 2)

        if(dist_centers + a_cyl.radius < self.radius and \
           dist_center_to_height < self.radius):

            return True
        
        else:

            return False

  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
    def does_intersect_sphere (self, other):

        # Makes sure that either sphere is not inside one another
        # this allows for quicker computation

        if(Sphere.is_inside_sphere(self, other) == False and \
           Sphere.is_inside_sphere(other, self) == False):


            dist_centers = self.center.distance(other.center)

            if(dist_centers - other.radius > self.radius):

                return False

            else:

                return True

        else:

            return False
        
  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
    def does_intersect_cube (self, a_cube):

        # Makes sure that the cube is not inside the sphere

        if(Sphere.is_inside_cube(self, a_cube) == False):

            dist_centers = self.center.distance(a_cube.center)

            if(dist_centers - a_cube.side / 2 > self.radius):

                return False

            else:

                return True

        else:

            return False


  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
    def circumscribe_cube (self):

        import math

        # Gives the largest cube that fits in the sphere by
        # claculating the larges possible cube side that fits
        # in the sphere and having the new cube share the same
        # center as the sphere, this was done by knowing that the
        # largest cube will have its diagnoal be the same lenght as
        # the diameter of the sphere

        self.diameter = 2 * self.radius

        self.largest_side = self.diameter / math.sqrt(3)

        return Cube(self.x, self.y, self.z, self.largest_side)

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):

        self.x = float(x)

        self.y = float(y)

        self.z = float(z)

        self.center = Point(self.x, self.y, self.z)

        self.side = float(side)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
    def __str__ (self):

        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + \
               '), Side: ' + str(self.side)

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
    def area (self):

        self.area = 6 * (self.side ** 2)

        return self.area

  # compute volume of a Cube
  # returns a floating point number
    def volume (self):

        self.volume = self.side ** 3

        return self.volume

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
    def is_inside_point (self, p):

        if(self.center.distance(p) < self.side / 2):

            return True

        else:

            return False

  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, a_sphere):

        dist_centers = self.center.distance(a_sphere.center)

        if(dist_centers + a_sphere.radius < self.side / 2):

            return True

        else:

            return False

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
    def is_inside_cube (self, other):

        dist_centers = self.center.distance(other.center)

        if(dist_centers + other.side / 2 < self.side / 2):

            return True

        else:

            return False
            
  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
    def is_inside_cylinder (self, a_cyl):

        dist_centers = self.center.distance(a_cyl.center)

        dist_center_to_height = math.hypot(dist_centers, a_cyl.height / 2)

        if(dist_centers + a_cyl.radius < self.side / 2 and \
           dist_center_to_height < self.side / 2):

            return True
        
        else:

            return False

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
    def does_intersect_cube (self, other):

        # Quick check to make sure that either cube is not inside
        # one another

        if(Cube.is_inside_cube(self, other) == False):

            dist_centers = self.center.distance(other.center)

            if(dist_centers - other.side / 2 > self.side / 2):

                return False

            else:

                return True

        else:

            return False
            
  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
    def intersection_volume (self, other):

        # Quick check to make sure that the cubes intersect

        if(Cube.does_intersect_cube(self, other) == False):

            return 0.0

        else:

            dist_centers = self.center.distance(other.center)

            dist_1 = dist_centers - self.side / 2

            dist_2 = dist_centers - other.side / 2

            intersect_dist = dist_centers - dist_1 - dist_2

            volume = intersect_dist ** 3

            return volume

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
    def inscribe_sphere (self):

        # The largest sphere will have its extremities in each dimension
        # touch the walls of the cube so the diameter is the side of the cube

        return Sphere(self.x, self.y, self.z, self.side / 2)

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):

        self.x = float(x)

        self.y = float(y)

        self.z = float(z)

        self.center = Point(self.x, self.y, self.z)

        self.radius = float(radius)

        self.height = float(height)

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):

        return 'Center: (' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + \
               '), Radius: ' + str(self.radius) + ', Height: ' + str(self.height)


  # compute surface area of Cylinder
  # returns a floating point number
    def area (self):

        import math

        self.area = (2 * math.pi) * ((self.radius ** 2) + (self.radius * self.height))

        return self.area

  # compute volume of a Cylinder
  # returns a floating point number
    def volume (self):

        import math

        self.volume = (math.pi * (self.radius ** 2) * self.height)

        return self.volume

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
    def is_inside_point (self, p):

        if(self.center.distance(p) < self.radius and \
           self.center.distance(p) < self.height / 2):

            return True

        else:

            return False
                
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
    def is_inside_sphere (self, a_sphere):

        dist_centers = self.center.distance(a_sphere.center)

        if(dist_centers + a_sphere.radius < self.radius and \
           dist_centers + a_sphere.radius < self.height / 2):

            return True

        else:

            return False
    

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
    def is_inside_cube (self, a_cube):

        import math

        # Quick check to make sure that the cube fits
        # inside the cylinder by checking for the largest
        # square that can be circumscribed by the cirle
        # face of the cylinder

        if(a_cube.side > (math.sqrt(2) * self.radius)):

            return False

        else:

            corner_1 = Point(a_cube.x + a_cube.side / 2, \
                             a_cube.y + a_cube.side / 2, \
                             a_cube.z + a_cube.side / 2)

            corner_2 = Point(a_cube.x + a_cube.side / 2, \
                             a_cube.y + a_cube.side / 2, \
                             a_cube.z - a_cube.side / 2)

            corner_3 = Point(a_cube.x + a_cube.side / 2, \
                             a_cube.y - a_cube.side / 2, \
                             a_cube.z + a_cube.side / 2)

            corner_4 = Point(a_cube.x + a_cube.side / 2, \
                             a_cube.y - a_cube.side / 2, \
                             a_cube.z - a_cube.side / 2)

            corner_5 = Point(a_cube.x - a_cube.side / 2, \
                             a_cube.y + a_cube.side / 2, \
                             a_cube.z + a_cube.side / 2)

            corner_6 = Point(a_cube.x - a_cube.side / 2, \
                             a_cube.y + a_cube.side / 2, \
                             a_cube.z - a_cube.side / 2)

            corner_7 = Point(a_cube.x - a_cube.side / 2, \
                             a_cube.y - a_cube.side / 2, \
                             a_cube.z + a_cube.side / 2)

            corner_8 = Point(a_cube.x - a_cube.side / 2, \
                             a_cube.y - a_cube.side / 2, \
                             a_cube.z - a_cube.side / 2)

            dist_centers = self.center.distance(a_cube.center)

            if(dist_centers + a_cube.side / 2 < self.radius and \
               dist_centers + a_cube.side / 2 < self.height / 2 and \
               self.center.distance(corner_1) < self.radius and \
               self.center.distance(corner_2) < self.radius and \
               self.center.distance(corner_3) < self.radius and \
               self.center.distance(corner_4) < self.radius and \
               self.center.distance(corner_5) < self.radius and \
               self.center.distance(corner_6) < self.radius and \
               self.center.distance(corner_7) < self.radius and \
               self.center.distance(corner_8) < self.radius):

                return True

            else:

                return False

            '''# Checks if the cube is inside the cylinder

            boolean_list = []

            if(self.x + self.radius > a_cube.x + a_cube.side / 2 and \
               self.x - self.radius < a_cube.x - a_cube.side / 2):

                boolean_list.append(True)

            else:

                boolean_list.append(False)

            if(self.y + self.radius > a_cube.y + a_cube.side / 2 and \
               self.y - self.radius < a_cube.y - a_cube.side / 2):

                boolean_list.append(True)

            else:

                boolean_list.append(False)

            if(self.z + self.height / 2 > a_cube.z + a_cube.side / 2 and \
               self.z - self.height / 2 < a_cube.z - a_cube.side / 2):

                boolean_list.append(True)

            else:

                boolean_list.append(False)

            if(False in boolean_list):

                return False

            else:

                return True'''

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
    def is_inside_cylinder (self, other):

        # Quick check that the other cylinder can fit
        # in this cylinder

        if(self.radius < other.radius or self.height < other.height):

            return False

        else:

            dist_centers = self.center.distance(other.center)

            if(dist_centers + other.radius < self.radius and \
               dist_centers + other.height / 2 < self.height / 2):

                return True

            else:

                return False

            '''# Checks that the other cylinder is insdie this
            # cylinder

            boolean_list = []

            if(self.x + self.radius > other.x + other.radius and \
               self.x - self.radius < other.x - other.radius):

                boolean_list.append(True)

            else:

                boolean_list.append(False)

            if(self.y + self.radius > other.y + other.radius and \
               self.y - self.radius < other.y - other.radius):

                boolean_list.append(True)

            else:

                boolean_list.append(False)

            if(self.z + self.height / 2 > other.z + other.height / 2 and \
               self.z - self.height / 2 < other.z - other.height / 2):

                boolean_list.append(True)

            else:

                boolean_list.append(False)

            if(False in boolean_list):

                return False

            else:

                return True'''

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
    def does_intersect_cylinder (self, other):

        # Quick check to make sure that the cylinders are not inside
        # one another

        if(Cylinder.is_inside_cylinder(self,other) == False and \
           Cylinder.is_inside_cylinder(other, self) == False):

            dist_centers = self.center.distance(other.center)

            if(dist_centers - other.radius  > self.radius and \
               dist_centers - other.height / 2 > self.height / 2):

                return True

            else:

                return False

            '''boolean_list = []

            # Checks that the other cylinder is outside of this cylinder
            # if not then they intersect

            if(self.x > other.x):

                if(self.x - self.radius > other.x + other.radius):

                    boolean_list.append(True)

                elif(self.x - self.radius < other.x + other.radius and \
                     self.z - self.height / 2 > other.z + other.height / 2 and \
                     self.z > other.z):

                    boolean_list.append(True)

                elif(self.x - self.radius < other.x + other.radius and \
                     self.z + self.height / 2 < other.z - other.height / 2 and \
                     self.z < other.z):

                    boolean_list.append(True)

                else:

                    boolean_list.append(False)

            else:

                if(self.x + self.radius < other.x - other.radius):

                    boolean_list.append(True)

                elif(self.x + self.radius > other.x - other.radius and \
                     self.z - self.height / 2 > other.z + other.height / 2 and \
                     self.z > other.z):

                    boolean_list.append(True)

                elif(self.x + self.radius > other.x - other.radius and \
                     self.z + self.height / 2 < other.z - other.height / 2 and \
                     self.z < other.z):

                    boolean_list.append(True)

                else:

                    boolean_list.append(False)

            if(self.y > other.y):

                if(self.y - self.radius > other.y + other.radius):

                    boolean_list.append(True)

                elif(self.y - self.radius < other.y + other.radius and \
                     self.z - self.height / 2 > other.z + other.height / 2 and \
                     self.z > other.z):

                    boolean_list.append(True)

                elif(self.y - self.radius < other.y + other.radius and \
                     self.z + self.height / 2 < other.z - other.height / 2 and \
                     self.z < other.z):

                    boolean_list.append(True)

                else:

                    boolean_list.append(False)

            else:

                if(self.y + self.radius < other.y - other.radius):

                    boolean_list.append(True)

                elif(self.y + self.radius > other.y - other.radius and \
                     self.z - self.height / 2 > other.z + other.height / 2 and \
                     self.z > other.z):

                    boolean_list.append(True)

                elif(self.y + self.radius > other.y - other.radius and \
                     self.z + self.height / 2 < other.z - other.height / 2 and \
                     self.z < other.z):

                    boolean_list.append(True)

                else:

                    boolean_list.append(False)

            if(self.z > other.z):

                if(self.z - self.height / 2 > other.z + other.height / 2):

                    boolean_list.append(True)

                else:

                    boolean_list.append(False)

            else:

                if(self.z + self.height / 2 < other.z - other.height / 2):

                    boolean_list.append(True)

                else:

                    boolean_list.append(False)

            if(False in boolean_list):

                return True

            else:

                return False'''

        else:

            return False

def main():

    import sys

    # Reads in the file data and gets rid of
    # any none relavent characters

    in_file = sys.stdin.readlines()

    for i in range(0, len(in_file)):

        in_file[i]= in_file[i].split(' ')

        for j in range(0, len(in_file[i])):

            if('\n' in in_file[i][j]):

                in_file[i][j].replace('\n', '')

  # read the coordinates of the first Point p

    p = in_file[0]

  # create a Point object

    p_object = Point(float(p[0]), float(p[1]), float(p[2]))

  # read the coordinates of the second Point q

    q = in_file[1]

  # create a Point object

    q_object = Point(float(q[0]), float(q[1]), float(q[2]))

  # read the coordinates of the center and radius of sphereA

    sphereA = in_file[2]

  # create a Sphere object

    sphereA_object = Sphere(float(sphereA[0]), float(sphereA[1]), float(sphereA[2]), float(sphereA[3]))

  # read the coordinates of the center and radius of sphereB

    sphereB = in_file[3]

  # create a Sphere object

    sphereB_object = Sphere(float(sphereB[0]), float(sphereB[1]), float(sphereB[2]), float(sphereB[3]))

  # read the coordinates of the center and side of cubeA

    cubeA = in_file[4]

  # create a Cube object

    cubeA_object = Cube(float(cubeA[0]), float(cubeA[1]), float(cubeA[2]), float(cubeA[3]))

  # read the coordinates of the center and side of cubeB

    cubeB = in_file[5]

  # create a Cube object

    cubeB_object = Cube(float(cubeB[0]), float(cubeB[1]), float(cubeB[2]), float(cubeB[3]))

  # read the coordinates of the center, radius and height of cylA

    cylA = in_file[6]

  # create a Cylinder object

    cylA_object = Cylinder(float(cylA[0]), float(cylA[1]), float(cylA[2]), float(cylA[3]), float(cylA[4]))

  # read the coordinates of the center, radius and height of cylB

    cylB = in_file[7]

  # create a Cylinder object

    cylB_object = Cylinder(float(cylB[0]), float(cylB[1]), float(cylB[2]), float(cylB[3]), float(cylB[4]))



    

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin

    origin = Point()

    p_dist = Point.distance(origin, p_object)

    q_dist = Point.distance(origin, q_object)

    if(p_dist > q_dist):

        print('Distance of Point p from the origin is greater than the distance of Point q from the origin')

    else:

        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

  # print if Point p is inside sphereA

    if(Sphere.is_inside_point(sphereA_object, p_object) == True):

        print('Point p is inside sphereA')

    else:

        print('Point p is not inside sphereA')

  # print if sphereB is inside sphereA

    if(Sphere.is_inside_sphere(sphereA_object, sphereB_object) == True):

        print('sphereB is inside sphereA')

    else:

        print('sphereB is not inside sphereA')

  # print if cubeA is inside sphereA

    if(Sphere.is_inside_cube(sphereA_object, cubeA_object) == True):

        print('cubeA is inside sphereA')

    else:

        print('cubeA is not inside sphereA')

  # print if cylA is inside sphereA

    if(Sphere.is_inside_cyl(sphereA_object, cylA_object) == True):

        print('cylA is inside sphereA')

    else:

        print('cylA is not inside sphereA')

  # print if sphereA intersects with sphereB

    if(Sphere.does_intersect_sphere(sphereA_object, sphereB_object) == True):

        print('sphereA does intersect sphereB')

    else:

        print('sphereA does not intersect sphereB')

  # print if cubeB intersects with sphereB

    if(Sphere.does_intersect_cube(sphereB_object, cubeB_object) == True):

        print('cubeB does intersect sphereB')

    else:

        print('cubeB does not intersect sphereB')

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA

    largest_cube = Sphere.circumscribe_cube(sphereA_object)

    if(Cube.volume(largest_cube) > Cylinder.volume(cylA_object)):

        print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')

    else:

        print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')

  # print if Point p is inside cubeA

    if(Cube.is_inside_point(cubeA_object, p_object) == True):

        print('Point p is inside cubeA')

    else:

        print('Point p is not inside cubeA')

  # print if sphereA is inside cubeA

    if(Cube.is_inside_sphere(cubeA_object, sphereA_object) == True):

        print('sphereA is inside cubeA')

    else:

        print('sphereA is not inside cubeA')

  # print if cubeB is inside cubeA

    if(Cube.is_inside_cube(cubeA_object, cubeB_object) == True):

        print('cubeB is inside cubeA')

    else:

        print('cubeB is not inside cubeA')

  # print if cylA is inside cubeA

    if(Cube.is_inside_cylinder(cubeA_object, cylA_object) == True):

        print('cylA is inside cubeA')

    else:

        print('cylA is not inside cubeA')

  # print if cubeA intersects with cubeB

    if(Cube.does_intersect_cube(cubeA_object, cubeB_object) == True):

        print('cubeA does intersect cubeB')

    else:

        print('cubeA does not intersect cubeB')

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA

    intersect_vol = Cube.intersection_volume(cubeA_object, cubeB_object)

    if(intersect_vol > Sphere.volume(sphereA_object)):

        print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')

    else:

        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA

    largest_SA = Cube.inscribe_sphere(cubeA_object)

    if(Sphere.area(largest_SA) > Cylinder.area(cylA_object) == True):

        print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')

    else:

        print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')

 

    

  # print if Point p is inside cylA

    if(Cylinder.is_inside_point(cylA_object, p_object) == True):

        print('Point p is inside cylA')

    else:

        print('Point p is not inside cylA')

  # print if sphereA is inside cylA

    if(Cylinder.is_inside_sphere(cylA_object, sphereA_object) == True):

        print('sphereA is inside cylA')

    else:

        print('sphereA is not inside cylA')

  # print if cubeA is inside cylA

    if(Cylinder.is_inside_cube(cylA_object, cubeA_object) == True):

        print('cubeA is inside cylA')

    else:

        print('cubeA is not inside cylA')
        
  # print if cylB is inside cylA

    if(Cylinder.is_inside_cylinder(cylA_object, cylB_object) == True):

        print('cylB is inside cylA')

    else:

        print('cylB is not inside cylA')

  # print if cylB intersects with cylA

    if(Cylinder.does_intersect_cylinder(cylA_object, cylB_object) == True):

        print('cylB does intersect cylA')

    else:

        print('cylB does not intersect cylA')

if __name__ == "__main__":
  main()
