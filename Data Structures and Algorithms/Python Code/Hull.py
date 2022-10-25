#  File: Hull.py

#  Description: The purpose of this program is to create a convex hull
#               from a set of given points. This program uses the Graham's scan
#               method to create the convex hull and return its area. We were
#               given pesudo code for Graham's scan method

#  Student Name: Michel Gonzalez

#  Student UT EID: Mag9989

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/23/2021

#  Date Last Modified: 06/23/2021

import sys

import math

# The Point calss was provided for this assigment

class Point (object):
    
    # constructor
  
    def __init__ (self, x = 0, y = 0):
        
        self.x = x
        
        self.y = y

    # get the distance to another Point object
  
    def dist (self, other):
      
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
  
    def __str__ (self):
      
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
  
    # Test if the points are equal
  
    def __eq__ (self, other):
      
        tol = 1.0e-8
        
        return ((abs(self.x - other.x) < tol) and \
                (abs(self.y - other.y) < tol))

    # Test if the points are not equal

    def __ne__ (self, other):
        
        tol = 1.0e-8
        
        return ((abs(self.x - other.x) >= tol) or \
                (abs(self.y - other.y) >= tol))

    # Test if this point is less than the other point

    def __lt__ (self, other):
        
        tol = 1.0e-8
        
        if (abs(self.x - other.x) < tol):
            
          if (abs(self.y - other.y) < tol):
              
            return False
        
          else:
              
            return (self.y < other.y)
        
        return (self.x < other.x)

    # Test if this point is less than or equal to
    # the pther point

    def __le__ (self, other):
        
        tol = 1.0e-8
        
        if (abs(self.x - other.x) < tol):
            
          if (abs(self.y - other.y) < tol):
              
            return True
        
          else:
              
            return (self.y <= other.y)
        
        return (self.x <= other.x)
    
    # Test if this point is greater than the other point
  
    def __gt__ (self, other):
        
        tol = 1.0e-8
        
        if (abs(self.x - other.x) < tol):
            
          if (abs(self.y - other.y) < tol):
              
            return False
        
          else:
              
            return (self.y > other.y)
        
        return (self.x > other.x)

    # Test if this point is greater than or equal to
    # the other point

    def __ge__ (self, other):
        
        tol = 1.0e-8
        
        if (abs(self.x - other.x) < tol):
            
          if (abs(self.y - other.y) < tol):
              
            return True
        
          else:
              
            return (self.y >= other.y)
        
        return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value

def det (p, q, r):

    # The determinant is calculated using the following matrix:
    # [1 p.x p.y]
    # [1 q.x q.y]
    # [1 r.x r.y]
    # If the determinant is negative then the point (r.x, r.y)
    # is to the right of the line made by the points (p.x, p.y)
    # & (q.x, q.y)

    determinant = 1 * (q.x * r.y - r.x * q.y) - \
                  p.x * (1 * r.y - 1 * q.y) + \
                  p.y * (1 * r.x - 1 * q.x)
                  
    return determinant

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull

def convex_hull (sorted_points):

    # This portion of the code was provided in instruction
    # format. This method looks at the last three points of
    # the sorted point list and if the determinant is negative
    # it keeps the points else it pops the second to last point
    # this gives back a list of points that are the furthest from the
    # origin compared to all other points

    upper_hull = []

    upper_hull.append(sorted_points[0])

    upper_hull.append(sorted_points[1])

    for i in range (2, len(sorted_points)):

        upper_hull.append(sorted_points[i])

        while (len(upper_hull) >= 3 and \
               det (upper_hull[len(upper_hull) - 3], \
                    upper_hull[len(upper_hull) - 2], \
                    upper_hull[len(upper_hull) - 1]) >= 0):

            upper_hull.pop(len(upper_hull) - 2)

    lower_hull = []

    lower_hull.append(sorted_points[len(sorted_points) - 1])

    lower_hull.append(sorted_points[len(sorted_points) - 2])

    for i in range (len(sorted_points) - 3, -1, -1):

        lower_hull.append(sorted_points[i])

        while (len(lower_hull) >= 3 and \
               det (lower_hull[len(lower_hull) - 3], \
                    lower_hull[len(lower_hull) - 2], \
                    lower_hull[len(lower_hull) - 1]) >= 0):

            lower_hull.pop(len(lower_hull) - 2)


    lower_hull.pop(0)

    lower_hull.pop(len(lower_hull) - 1)

    for i in range(0, len(lower_hull)):

        upper_hull.append(lower_hull[i])

    convex_hull = upper_hull.copy()

    return convex_hull


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon

def area_poly (convex_poly):

    # This portion was also provided in the assigment
    # by calcualting the determinant of all the points
    # that make the convex hull.
    # I created two seperate determinant values and subtarcted them
    # after their summations

    det_1 = 0

    det_2 = 0

    for i in range(0, len(convex_poly)):

        if(i != len(convex_poly) - 1):

            det_1 += convex_poly[i].x * convex_poly[i + 1].y

            det_2 += convex_poly[i].y * convex_poly[i + 1].x

        else:

            # The last point and the first point have a determinant
            # this if-else statment takes care of this

            det_1 += convex_poly[i].x * convex_poly[0].y

            det_2 += convex_poly[i].y * convex_poly[0].x


    # calcualtes the actual determinant of the points
    # and returns the area

    determinant = det_1 - det_2

    area = (1/2) * abs(determinant)
    
    return area

# Input: no input
# Output: a string denoting all test cases have passed

def test_cases():
    
    # write your own test cases

    assert convex_hull([Point(0,0), Point(0,1), Point(0,.5), Point(1,0),]) == \
           [Point(0,0), Point(0,1), Point(1,0)]

    assert convex_hull([Point(0,0), Point(0,1), Point(1,0), Point(1,1)]) == \
           [Point(0,0), Point(0,1), Point(1,0), Point(1,1)]

    assert area_poly([Point(0,0), Point(0,1), Point(1,0)]) == 0.5

    assert area_poly([Point(0,0), Point(0,1), Point(1,0), Point(1,1)]) == 1


    return "all test cases passed"

def main():
    
    # create an empty list of Point objects
  
    points_list = []

    # read number of points
  
    line = sys.stdin.readline()
  
    line = line.strip()
  
    num_points = int (line)

    # read data from standard input
  
    for i in range (num_points):

        line = sys.stdin.readline()
    
        line = line.strip()
    
        line = line.split()
    
        x = int (line[0])
    
        y = int (line[1])
    
        points_list.append (Point (x, y))

    # sort the list according to x-coordinates
  
    sorted_points = sorted (points_list)

    '''# print the sorted list of Point objects
  
    for p in sorted_points:
      
        print (str(p))'''

    # get the convex hull

    convex = convex_hull (sorted_points)

    # run your test cases

    # print your results to standard output

    # print the convex hull

    print('Convex Hull')

    for i in convex:

        print('(' + str(i.x) + ', ' + str(i.y) + ')' )

    # get the area of the convex hull

    area = area_poly(convex)

    # print the area of the convex hull

    print()

    print('Area of Convex Hull =', area)

if __name__ == "__main__":
  main()
