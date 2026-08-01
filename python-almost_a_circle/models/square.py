#!/usr/bin/python3
"""This module defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square, which is a rectangle with equal sides."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square with validated attributes."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, updating width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to the attributes of the square."""
        if args and len(args) > 0:
            names = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(names):
                    setattr(self, names[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

