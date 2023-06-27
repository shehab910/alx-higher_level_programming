#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class Square defines a square
    This class has no public attributes
    """

    def __init__(self, size):
        """This __init__ method initialize an instance with a private
        instance attribute called size (with type and value verification)
        """
        self.__size = size
