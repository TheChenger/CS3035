"""
Cameron Cheng

CS3035-01
cylinder.py inherits from the Shape3D class and then adds more methods
"""
import math

from shape3d import Shape3d

class Cylinder(Shape3d):

    """
    This is our cylinder class which inherits from the Shape3D class
    """

    def __init__(self, color = 'black', transparency = 0.0, radius = 0.0, height = 0.0):
        """
        :param color:
        :param transparency:
        :param radius:
        :param height:
        """
        super().__init__(color, transparency)
        self.__radius = radius
        self.__height = height

    def get_radius(self):
        """
        Method to return the radius of the cylinder
        :return:
        """
        return self.radius

    def set_radius(self, x):
        """
        Method to set the radius of the cylinder
        :param x:
        :return:
        """
        self.radius = x

    def get_height(self):
        """
        Method to return the height of the cylinder
        :return:
        """
        return self.height

    def set_height(self, x):
        """
        Method to set the height of the cylinder
        :param x:
        :return:
        """
        self.height = x

    def area(self):
        """
        Method to return the area of the cylinder
        :return:
        """
        area = (2 * math.pi * (math.pow(self.__radius, 2))) + 2 * math.pi * self.__radius * self.__height
        return area

    def volume(self):
        """
        Method to return the volume of the cylinder
        :return:
        """
        volume = math.pi * math.pow(self.__radius, 2) * self.__height
        return volume

    def __str__(self):
        """
        Overloaded __str__ method gives the ability to print out our cylinder object
        :return:
        """
        return f'{super().__str__()}, radius = {self.__radius}, height = {self.__height}'

    def __repr__(self):
        """
        Overloaded __repr__ method gives the ability to print out our cylinder object
        :return:
        """
        return f'{super().__str__()}, radius = {self.__radius}, height = {self.__height}'