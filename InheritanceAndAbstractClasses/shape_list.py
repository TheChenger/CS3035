"""
Cameron Cheng

CS3035-01
shape_list.py is the module that allows the objects to be placed into a list
and allows various operations to be done to it and the individual objects
"""

import cylinder
import pyramid


class ShapeList(list):

    def __init__(self):
        pass

    def average_area_of_cylinders(self):
        """
        Method to return the average area of the CYLINDERS in the list
        :return:
        """
        totalArea = 0
        numOfC = 0
        for i in range(len(self)):
            if type(self[i]) == cylinder.Cylinder:
                numOfC += 1
                totalArea += self[i].area()

        return totalArea / numOfC

    def average_area_of_pyramids(self):
        """
        Method to return the average area of the PYRAMIDS in the list
        :return:
        """
        totalArea = 0
        numOfP = 0
        for i in range(len(self)):
            if type(self[i]) == pyramid.Pyramid:
                numOfP += 1
                totalArea += self[i].area()

        return totalArea / numOfP

    def max_volume(self):
        """
        Method that returns the largest volume in the list of shapes
        :return:
        """
        highVolume = 0
        for i in range(len(self)-1):
            if highVolume < self[i].volume():
                highVolume = self[i].volume()

        return highVolume

    def min_volume(self):
        """
        Method that returns the smallest volume in the list of shapes
        :return:
        """

        minVolume = self[1].volume()

        for i in range(len(self)):
            if minVolume > self[i].volume():
                minVolume = self[i].volume()

        return minVolume

    def display_cylinders(self):
        """
        Method to display (print) all the CYLINDERS in the list of shapes
        :return:
        """
        for i in range(len(self)):
            if type(self[i]) == cylinder.Cylinder:
                print(self[i])
            else:
                pass


    def display_pyramids(self):
        """
        Method to display (print) all the PYRAMIDS in the list of shapes
        :return:
        """
        for i in range(len(self)):
            if type(self[i]) == pyramid.Pyramid:
                print(self[i])
            else:
                pass