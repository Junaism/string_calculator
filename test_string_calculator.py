import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    """Test class for unit tests of string calculator"""

    def setUp(self) -> None:
        self.calculator = StringCalculator()
        return super().setUp()

    def test_basic_calulation(self):
        """check basic addition is working fine"""
        self.assertEqual(4+5, self.calculator.add("4,5"))
        self.assertEqual(-1, self.calculator.add(""))
        self.assertEqual(3, self.calculator.add("3,"))
        self.assertEqual(3, self.calculator.add(",3"))
        self.assertEqual(1+2+4+6+7+9+56, self.calculator.add("1,2,4,6,7,9,56"))
        self.assertEqual(4+5, self.calculator.add("4,\\n5"))
        self.assertEqual(3+9, self.calculator.add("3,9\\n"))
        self.assertEqual(3+9, self.calculator.add("\\n3,9\\n"))
        self.assertEqual(3+9+8, self.calculator.add("\\n3,9\\n8"))
    
    def test_error_are_handled_properly(self):
        """check validation errors are handled properly"""
        self.assertRaises(TypeError, self.calculator.add, "fr,56")
        self.assertRaises(TypeError, self.calculator.add, "f,9.0")
        self.assertRaises(TypeError, self.calculator.add, "f,9.0\br")
        self.assertRaises(TypeError, self.calculator.add, "f\b9\\")

    def test_alert_messages(self):
        """test alert messages"""
        with self.assertRaises(ValueError) as msg:
            self.calculator.add("5,-9")
            self.assertEqual(msg, "negative numbers not allowed -6")
        with self.assertRaises(ValueError) as msg:
            self.calculator.add("5,-6\\n-7")
            self.assertEqual(msg, "negative numbers not allowed -6,-7")
