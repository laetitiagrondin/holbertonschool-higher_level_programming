#!/usr/bin/python3
"""
Unittest for max_integer([..]).
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for the max_integer function.
    """

    def test_ordered_list(self):
        """
        Test an ordered list.
        """
        self.assertEqual(max_integer([5, 10, 15, 20]), 20)

    def test_unordered_list(self):
        """
        Test an unordered list.
        """
        self.assertEqual(max_integer([12, 7, 19, 3]), 19)

    def test_max_at_beginning(self):
        """
        Test a list with the max at the beginning.
        """
        self.assertEqual(max_integer([99, 50, 20, 10]), 99)

    def test_empty_list(self):
        """
        Teste an empty list.
        """
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """
        Test a list with a single element.
        """
        self.assertEqual(max_integer([42]), 42)

    def test_floats(self):
        """
        Test a list with floating point numbers.
        """
        self.assertEqual(max_integer([3.14, 2.71, 6.28, -1.5]), 6.28)

    def test_ints_and_floats(self):
        """
        Test a list with mixed integers and floats.
        """
        self.assertEqual(max_integer([1.5, 20, 3.3, 19]), 20)

    def test_string(self):
        """
        Test a string argument (should return the max caracter).
        """
        self.assertEqual(max_integer("OpenAI"), 'p')

    def test_list_of_strings(self):
        """
        Test a list of strings.
        """
        self.assertEqual(max_integer(["abc", "def"]), "def")

    def test_none_argument(self):
        """
        Test passing None (should raise a TypeError).
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negative_numbers(self):
        """
        Test a list with only negative numbers.
        """
        self.assertEqual(max_integer([-10, -20, -5, -30]), -5)


if __name__ == '__main__':
    unittest.main()
