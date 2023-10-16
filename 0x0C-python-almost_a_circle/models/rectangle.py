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

    def __str__(self):
        """return returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "\
            f"{self.__width}/{self.__height}"

    def display(self):
        """Width."""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """ update """

        list = [self.id, self.__width, self.__height, self.__x, self.__y]
        for x, arg in enumerate(args):
            list[x] = arg
            if x == 4:
                break

        super().__init__(list[0])
        self.width = list[1]
        self.height = list[2]
        self.x = list[3]
        self.y = list[4]

    def update(self, *args, **kwargs):
        """Width."""
        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)
        else:
            for key, value1 in kwargs.items():
                setattr(self, key, value1)

    def to_dictionary(self):
        """Width."""
        dic = dict()
        dic['width'] = self.width
        dic['height'] = self.height
        dic['id'] = self.id
        dic['x'] = self.x
        dic['y'] = self.y
        return (dic)
