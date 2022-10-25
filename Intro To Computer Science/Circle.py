import math

class Circle:

    def __init__(self, rad = 1):

        self.__radius = rad

    def getRadius(self):

        return self.__radius

    def setRadius(self, rad):

        self.__radius = rad

    def getPerimeter(self):

        return 2 * math.pi * self.__radius

    def getArea(self):

        return math.pi * (self.__radius ** 2)
