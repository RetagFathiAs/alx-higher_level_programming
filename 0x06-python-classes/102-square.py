#!/usr/bin/python3
""" MagicClass"""
import math


class MagicClass:
    """ represents a circle"""
    def __init__(self, radius=0):
        """Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circumference of the circle"""
        return 2 * math.pi * self.__radius
