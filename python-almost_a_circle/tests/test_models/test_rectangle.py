#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test the creation of Rectangle instances."""

    def test_is_base(self):
        """Test that a Rectangle is a Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        """Test creating a rectangle with a width and a height."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_position(self):
        """Test that x and y default to zero."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_all_args(self):
        """Test creating a rectangle with every argument."""
        r = Rectangle(10, 2, 3, 4, 89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_id_auto_increment(self):
        """Test that ids increment when none is given."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_no_args(self):
        """Test that creating without arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test that a missing height raises a TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_width_is_private(self):
        """Test that width is a private attribute."""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2).__width)


class TestRectangleWidth(unittest.TestCase):
    """Test the validation of the width attribute."""

    def test_string(self):
        """Test that a string width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_float(self):
        """Test that a float width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2)

    def test_none(self):
        """Test that a None width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_list(self):
        """Test that a list width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 2)

    def test_zero(self):
        """Test that a zero width raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative(self):
        """Test that a negative width raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_setter(self):
        """Test that the setter validates too."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -1


class TestRectangleHeight(unittest.TestCase):
    """Test the validation of the height attribute."""

    def test_string(self):
        """Test that a string height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_none(self):
        """Test that a None height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_zero(self):
        """Test that a zero height raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_negative(self):
        """Test that a negative height raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)


class TestRectangleX(unittest.TestCase):
    """Test the validation of the x attribute."""

    def test_string(self):
        """Test that a string x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_dict(self):
        """Test that a dictionary x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_negative(self):
        """Test that a negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_zero_is_valid(self):
        """Test that zero is a valid x."""
        self.assertEqual(Rectangle(10, 2, 0).x, 0)


class TestRectangleY(unittest.TestCase):
    """Test the validation of the y attribute."""

    def test_string(self):
        """Test that a string y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_negative(self):
        """Test that a negative y raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_zero_is_valid(self):
        """Test that zero is a valid y."""
        self.assertEqual(Rectangle(10, 2, 3, 0).y, 0)


class TestRectangleArea(unittest.TestCase):
    """Test the area method."""

    def test_small(self):
        """Test the area of a small rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_large(self):
        """Test the area of a large rectangle."""
        self.assertEqual(Rectangle(999, 999).area(), 998001)

    def test_square_shape(self):
        """Test the area when width equals height."""
        self.assertEqual(Rectangle(7, 7).area(), 49)

    def test_takes_no_argument(self):
        """Test that area accepts no argument."""
        with self.assertRaises(TypeError):
            Rectangle(3, 2).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Test the display method."""

    def capture(self, rect):
        """Return what a rectangle prints when displayed."""
        captured = io.StringIO()
        sys.stdout = captured
        rect.display()
        sys.stdout = sys.__stdout__
        return captured.getvalue()

    def test_simple(self):
        """Test displaying a rectangle without a position."""
        self.assertEqual(self.capture(Rectangle(2, 2)), "##\n##\n")

    def test_one_by_one(self):
        """Test displaying the smallest rectangle."""
        self.assertEqual(self.capture(Rectangle(1, 1)), "#\n")

    def test_with_x(self):
        """Test that x adds spaces before each row."""
        self.assertEqual(self.capture(Rectangle(2, 1, 2)), "  ##\n")

    def test_with_y(self):
        """Test that y adds new lines before the rectangle."""
        self.assertEqual(self.capture(Rectangle(2, 1, 0, 2)), "\n\n##\n")

    def test_with_x_and_y(self):
        """Test displaying a rectangle with both offsets."""
        self.assertEqual(self.capture(Rectangle(2, 2, 2, 2)),
                         "\n\n  ##\n  ##\n")


class TestRectangleStr(unittest.TestCase):
    """Test the __str__ method."""

    def test_full(self):
        """Test the string of a rectangle with every attribute."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_default_position(self):
        """Test the string of a rectangle without a position."""
        r = Rectangle(5, 5, 1, 0, 7)
        self.assertEqual(str(r), "[Rectangle] (7) 1/0 - 5/5")

    def test_print(self):
        """Test that print uses the string representation."""
        captured = io.StringIO()
        sys.stdout = captured
        print(Rectangle(2, 3, 0, 0, 1))
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "[Rectangle] (1) 0/0 - 2/3\n")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Test the update method with no keyword arguments."""

    def test_id(self):
        """Test updating only the id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_id_width(self):
        """Test updating the id and the width."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_all(self):
        """Test updating every attribute."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_no_args(self):
        """Test that updating with nothing changes nothing."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_too_many_args(self):
        """Test that extra arguments are ignored."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_invalid_width(self):
        """Test that update validates the width."""
        r = Rectangle(10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Test the update method with keyword arguments."""

    def test_one(self):
        """Test updating a single attribute by name."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")

    def test_several(self):
        """Test updating several attributes by name."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/10")

    def test_order_does_not_matter(self):
        """Test that the order of keyword arguments is free."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")

    def test_args_wins(self):
        """Test that keyword arguments are skipped when args exist."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=99)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_unknown_key(self):
        """Test that an unknown key is simply set."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(unknown=5)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_invalid_value(self):
        """Test that update validates keyword values."""
        r = Rectangle(10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)


class TestRectangleToDictionary(unittest.TestCase):
    """Test the to_dictionary method."""

    def test_type(self):
        """Test that the result is a dictionary."""
        self.assertEqual(type(Rectangle(10, 2, 1, 9).to_dictionary()), dict)

    def test_keys(self):
        """Test that every expected key is present."""
        d = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertEqual(sorted(d.keys()),
                         ["height", "id", "width", "x", "y"])

    def test_values(self):
        """Test that the values match the attributes."""
        d = Rectangle(10, 2, 1, 9, 1).to_dictionary()
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_used_with_update(self):
        """Test that the dictionary can update another rectangle."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))

    def test_not_the_same_object(self):
        """Test that updating from a dictionary makes a distinct object."""
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertIsNot(r1, r2)


if __name__ == "__main__":
    unittest.main()
