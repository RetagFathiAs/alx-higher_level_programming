#!/usr/bin/python3
""" forth task """"


class Square:
    """square"""

    def __init__(self, size=0):
        """Init the square classs
        Args:
        param1: size is the type int attribute to make it private
        """
        if not isinstance(size, int):
            raise TypeError("size mut be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area"""
        return (self.__size * self.__size)
