"""
Cameron Cheng

CS3035-01
pyramid.py inherits from the Shape3D class and then adds more methods
"""
import math

from shape3d import Shape3d

class Pyramid(Shape3d):
    """
    This is our pyramid class which inherits from the Shape3D class
    """
    def __init__(self, color = 'black', transparency = 0.0, base = 0.0, height = 0.0, slant = 0.0):
        """

        :param color:
        :param transparency:
        :param base:
        :param height:
        :param slant:
        """
        super().__init__(color, transparency)
        self.__base = base
        self.__height = height
        self.__slant = slant

    def get_base(self):
        """
        Method to return the base of the pyramid
        :return:
        """
        return self.__base
    def get_height(self):
        """
        Method to return the height of the pyramid
        :return:
        """
        return self.__height
    def get_slant(self):
        """
        Method to return the slant of the pyramid
        :return:
        """
        return self.__slant

    def set_base(self, x):
        """
        Method to set the base of the pyramid
        :param x:
        :return:
        """
        self.__base = x
    def set_height(self,x):
        """
        Method to set the height of the pyramid
        :param x:
        :return:
        """
        self.__height = x
    def set_slant(self,x):
        """
        Method to set the slant of the pyramid
        :param x:
        :return:
        """
        self.__slant = x

    def area(self):
        """
        Method to return the area of the area of the pyramid
        :return:
        """
        return 2 * self.__base * self.__slant + math.pow(self.__base, 2)

    def volume(self):
        """
        Method to return the volume of the pyramid
        :return:
        """
        return 1/3 * math.pow(self.__base,2) * self.__height

    def __str__(self):
        """
        Overloaded __str__ method to be able to print the pyramid object
        :return:
        """
        return f'{super().__str__()}, base = {self.__base}, height = {self.__height}, slant = {self.__slant}'

    def __repr__(self):
        """
        Overloaded __repr__ method to be able to print the pyramid object
        :return:
        """
        return f'{super().__str__()}, base = {self.__base}, height = {self.__height}, slant = {self.__slant}'