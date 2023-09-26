#!/usr/bin/python3
""" Square class """


class Square:
    """Square"""
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
