"""
Cameron Cheng

CS3035-01
shape3D.py is our base class that our shape classes inherit from
"""
from abc import ABC, abstractmethod


class Shape3d:
    def __init__(self, color = 'Black', transparency = 0.0):
        """

        :param color:
        :param transparency:
        """
        self.__color = color
        self.__transparency = transparency

    def get_color(self):
        """
        Method to return the color of the shape
        :return:
        """
        return self.__color

    def get_transparency(self):
        """
        Method to return the transparency of the shape
        :return:
        """
        return self.__transparency

    def set_color(self, x):
        """
        Method to set the color of the shape
        :param x:
        :return:
        """
        self.__color = x

    def set_transparency(self, x):
        """
        Method to set the transparency of the shape
        :param x:
        :return:
        """
        self.__transparency = x

    @abstractmethod
    def area(self):

        pass

    @abstractmethod
    def volume(self):
        pass

    def __str__(self):
        """
        Overloaded __str__ method to be able to print the shape3d object
        :return:
        """
        return f'Color = {self.__color}, Transparency = {self.__transparency}'

    def __repr__(self):
        """
        Overloaded __repr__ method to be able to print the shape3d object
        :return:
        """
        return f'Color = {self.__color}, Transparency = {self.__transparency}'
