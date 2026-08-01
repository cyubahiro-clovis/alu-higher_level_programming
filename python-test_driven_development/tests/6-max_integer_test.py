#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test a list already in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list where the max is in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test that an empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test that calling without an argument returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list containing only negative numbers."""
        self.assertEqual(max_integer([-3, -1, -7]), -1)

    def test_mixed_signs(self):
        """Test a list containing positive and negative numbers."""
        self.assertEqual(max_integer([-5, 0, 5]), 5)

    def test_duplicated_max(self):
        """Test a list where the max appears more than once."""
        self.assertEqual(max_integer([4, 4, 2]), 4)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.5, 3.7, 2.2]), 3.7)

    def test_mixed_numbers(self):
        """Test a list mixing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_strings(self):
        """Test a list of strings, compared alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_one_string(self):
        """Test that a string is treated as a list of characters."""
        self.assertEqual(max_integer("hello"), "o")

    def test_mixed_types_raises(self):
        """Test that comparing a string and an integer raises."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_none_raises(self):
        """Test that passing None raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
