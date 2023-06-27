#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class Square defines a square
    This class has no public attributes
    """

    def __init__(self, size=0):
        """This __init__ method initialize an instance with a private
        instance attribute called size (with type and value verification)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """This public instance method returns the current square area"""
        return self.__size ** 2
