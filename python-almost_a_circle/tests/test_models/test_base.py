#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Test the creation of Base instances."""

    def test_id_auto_increment(self):
        """Test that ids increment when no id is given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_given(self):
        """Test that a given id is used as it is."""
        self.assertEqual(Base(89).id, 89)

    def test_id_none(self):
        """Test that None triggers the auto increment."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_negative(self):
        """Test that a negative id is accepted."""
        self.assertEqual(Base(-5).id, -5)

    def test_id_zero(self):
        """Test that zero is accepted as an id."""
        self.assertEqual(Base(0).id, 0)

    def test_id_string(self):
        """Test that a string id is accepted."""
        self.assertEqual(Base("hello").id, "hello")

    def test_nb_objects_is_private(self):
        """Test that nb_objects is a private class attribute."""
        with self.assertRaises(AttributeError):
            print(Base.nb_objects)

    def test_two_args(self):
        """Test that passing two arguments raises a TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Test the to_json_string static method."""

    def test_none(self):
        """Test that None returns an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Test that an empty list returns an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_type(self):
        """Test that the result is a string."""
        d = Rectangle(10, 7, 2, 8).to_dictionary()
        self.assertEqual(type(Base.to_json_string([d])), str)

    def test_one_dictionary(self):
        """Test a list holding a single dictionary."""
        d = {"id": 1, "width": 2}
        self.assertEqual(Base.to_json_string([d]),
                         '[{"id": 1, "width": 2}]')

    def test_two_dictionaries(self):
        """Test a list holding two dictionaries."""
        d = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 1}, {"id": 2}]')


class TestBaseFromJsonString(unittest.TestCase):
    """Test the from_json_string static method."""

    def test_none(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_type(self):
        """Test that the result is a list."""
        s = '[{"id": 89}]'
        self.assertEqual(type(Base.from_json_string(s)), list)

    def test_one_dictionary(self):
        """Test a JSON string holding one dictionary."""
        s = '[{"id": 89, "width": 10}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 89, "width": 10}])

    def test_two_dictionaries(self):
        """Test a JSON string holding two dictionaries."""
        s = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.from_json_string(s), [{"id": 1}, {"id": 2}])


class TestBaseSaveToFile(unittest.TestCase):
    """Test the save_to_file class method."""

    def tearDown(self):
        """Remove any file created by a test."""
        for name in ("Rectangle.json", "Square.json", "Base.json"):
            try:
                os.remove(name)
            except IOError:
                pass

    def test_none(self):
        """Test that None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_empty_list(self):
        """Test that an empty list writes an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_one_rectangle(self):
        """Test writing a single rectangle."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 2)

    def test_one_square(self):
        """Test that the file is named after the class."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_overwrite(self):
        """Test that an existing file is overwritten."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8, 1)])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestBaseCreate(unittest.TestCase):
    """Test the create class method."""

    def test_rectangle(self):
        """Test creating a rectangle from a dictionary."""
        r = Rectangle(3, 5, 1, 0, 1)
        new = Rectangle.create(**r.to_dictionary())
        self.assertEqual(str(new), "[Rectangle] (1) 1/0 - 3/5")

    def test_rectangle_is_new_object(self):
        """Test that create returns a different object."""
        r = Rectangle(3, 5, 1)
        new = Rectangle.create(**r.to_dictionary())
        self.assertIsNot(r, new)

    def test_square(self):
        """Test creating a square from a dictionary."""
        s = Square(5, 1, 0, 1)
        new = Square.create(**s.to_dictionary())
        self.assertEqual(str(new), "[Square] (1) 1/0 - 5")

    def test_square_is_new_object(self):
        """Test that create returns a different square object."""
        s = Square(5)
        new = Square.create(**s.to_dictionary())
        self.assertIsNot(s, new)


class TestBaseLoadFromFile(unittest.TestCase):
    """Test the load_from_file class method."""

    def tearDown(self):
        """Remove any file created by a test."""
        for name in ("Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except IOError:
                pass

    def test_no_file(self):
        """Test that a missing file returns an empty list."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_type(self):
        """Test that the loaded objects are rectangles."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        loaded = Rectangle.load_from_file()
        self.assertEqual(type(loaded[0]), Rectangle)

    def test_square_type(self):
        """Test that the loaded objects are squares."""
        Square.save_to_file([Square(10, 2, 8)])
        loaded = Square.load_from_file()
        self.assertEqual(type(loaded[0]), Square)

    def test_content(self):
        """Test that the loaded rectangles match the saved ones."""
        r = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(str(loaded[0]), str(r))


if __name__ == "__main__":
    unittest.main()
