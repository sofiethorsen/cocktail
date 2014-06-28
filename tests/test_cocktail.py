import unittest

from cocktail import main

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = main.Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)