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