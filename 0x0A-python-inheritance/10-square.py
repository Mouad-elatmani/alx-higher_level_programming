#!/usr/bin/python3
"""Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)