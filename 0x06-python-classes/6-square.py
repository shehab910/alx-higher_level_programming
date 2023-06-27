#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class Square defines a square
    This class has no public attributes
    """

    def __init__(self, size=0, position=(0, 0)):
        """This __init__ method initialize an instance with a private
        instance attribute called size (with type and value verification)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """This getter method retrieve the value of the private attribute
        size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """This setter method set the value of the private attribute
        size (with type and value verification)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """This getter method retrieve the value of the private attribute
        position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This setter method set the value of the private attribute
        position (with type and value verification)
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This public instance method returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This public instance method prints in stdout the square with the
        character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
