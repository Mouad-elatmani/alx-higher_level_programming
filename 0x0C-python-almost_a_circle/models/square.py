#!/usr/bin/python3

"""models/Square.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Width."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Width."""
        return self.width

    @size.setter
    def size(self, value):
        """Width."""
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """Width."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
