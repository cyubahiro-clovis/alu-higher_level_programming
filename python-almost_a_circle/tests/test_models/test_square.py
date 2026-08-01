#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Test the creation of Square instances."""

    def test_is_rectangle(self):
        """Test that a Square is a Rectangle."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_base(self):
        """Test that a Square is a Base."""
        self.assertIsInstance(Square(5), Base)

    def test_one_arg(self):
        """Test creating a square with only a size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_position(self):
        """Test that x and y default to zero."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_all_args(self):
        """Test creating a square with every argument."""
        s = Square(5, 2, 3, 89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_id_auto_increment(self):
        """Test that ids increment when none is given."""
        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s2.id, s1.id + 1)

    def test_no_args(self):
        """Test that creating without a size raises a TypeError."""
        with self.assertRaises(TypeError):
            Square()

    def test_no_new_attribute(self):
        """Test that a square has no private size attribute."""
        s = Square(5)
        self.assertNotIn("_Square__size", s.__dict__)


class TestSquareValidation(unittest.TestCase):
    """Test that a Square validates like a Rectangle."""

    def test_string_size(self):
        """Test that a string size raises a width TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_none_size(self):
        """Test that a None size raises a width TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_zero_size(self):
        """Test that a zero size raises a width ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_size(self):
        """Test that a negative size raises a width ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_string_x(self):
        """Test that a string x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "2")

    def test_negative_x(self):
        """Test that a negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -2)

    def test_negative_y(self):
        """Test that a negative y raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -3)


class TestSquareSize(unittest.TestCase):
    """Test the size getter and setter."""

    def test_getter(self):
        """Test that the getter returns the width."""
        self.assertEqual(Square(5).size, 5)

    def test_setter(self):
        """Test that the setter changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_setter_string(self):
        """Test that the setter validates the type."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_zero(self):
        """Test that the setter refuses zero."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_setter_negative(self):
        """Test that the setter refuses negative values."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -3


class TestSquareArea(unittest.TestCase):
    """Test the inherited area method."""

    def test_small(self):
        """Test the area of a small square."""
        self.assertEqual(Square(5).area(), 25)

    def test_one(self):
        """Test the area of the smallest square."""
        self.assertEqual(Square(1).area(), 1)

    def test_after_resize(self):
        """Test that the area follows a size change."""
        s = Square(5)
        s.size = 3
        self.assertEqual(s.area(), 9)


class TestSquareDisplay(unittest.TestCase):
    """Test the inherited display method."""

    def capture(self, square):
        """Return what a square prints when displayed."""
        captured = io.StringIO()
        sys.stdout = captured
        square.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_simple(self):
        """Test displaying a square without a position."""
        self.assertEqual(self.capture(Square(2)), "##\n##\n")

    def test_with_x(self):
        """Test that x adds spaces before each row."""
        self.assertEqual(self.capture(Square(2, 2)), "  ##\n  ##\n")

    def test_with_y(self):
        """Test that y adds new lines before the square."""
        self.assertEqual(self.capture(Square(2, 0, 1)), "\n##\n##\n")


class TestSquareStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_full(self):
        """Test the string of a square with every attribute."""
        self.assertEqual(str(Square(5, 2, 1, 12)), "[Square] (12) 2/1 - 5")

    def test_default_position(self):
        """Test the string of a square without a position."""
        self.assertEqual(str(Square(5, 0, 0, 7)), "[Square] (7) 0/0 - 5")


class TestSquareUpdateArgs(unittest.TestCase):
    """Test the update method with no keyword arguments."""

    def test_id(self):
        """Test updating only the id."""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")

    def test_id_size(self):
        """Test updating the id and the size."""
        s = Square(5)
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

    def test_all(self):
        """Test updating every attribute."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_no_args(self):
        """Test that updating with nothing changes nothing."""
        s = Square(5, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_invalid_size(self):
        """Test that update validates the size."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "invalid")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Test the update method with keyword arguments."""

    def test_x(self):
        """Test updating only x by name."""
        s = Square(5, 0, 0, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")

    def test_size_and_y(self):
        """Test updating the size and y by name."""
        s = Square(5, 0, 0, 1)
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 0/1 - 7")

    def test_with_id(self):
        """Test updating the id by name."""
        s = Square(5)
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 0/1 - 7")

    def test_args_wins(self):
        """Test that keyword arguments are skipped when args exist."""
        s = Square(5)
        s.update(89, 2, size=99)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")


class TestSquareToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_type(self):
        """Test that the result is a dictionary."""
        self.assertEqual(type(Square(10, 2, 1).to_dictionary()), dict)

    def test_keys(self):
        """Test that every expected key is present."""
        d = Square(10, 2, 1, 1).to_dictionary()
        self.assertEqual(sorted(d.keys()), ["id", "size", "x", "y"])

    def test_values(self):
        """Test that the values match the attributes."""
        d = Square(10, 2, 1, 1).to_dictionary()
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_used_with_update(self):
        """Test that the dictionary can update another square."""
        s1 = Square(10, 2, 1, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))

    def test_not_the_same_object(self):
        """Test that updating from a dictionary makes a distinct object."""
        s1 = Square(10, 2, 1, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertIsNot(s1, s2)


if __name__ == "__main__":
    unittest.main()

