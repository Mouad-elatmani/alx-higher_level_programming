#!/usr/bin/python3
"""models/rectangle.py"""


from models.base import Base


class Rectangle(Base):
    """
    This class allows you to create and manipulate Rectangle objects.
    Each Rectangle is defined by its width and height
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getters"""
        return self.__width

    @property
    def height(self):
        """height getters"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Width."""
        return self.__x

    @property
    def y(self):
        """Width."""
        return self.__y

    @x.setter
    def x(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Width."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate and returns the rectangle area """
        return (self.__width * self.__height)

    def display(self):
        """ print a rectangle using the "#" character
            based on its width and height """
        rect = ""
        for _ in range(self.__height):
            rect += "#" * self.__width + "\n"
        print(rect, end="")
