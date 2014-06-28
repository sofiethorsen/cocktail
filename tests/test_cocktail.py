#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os

from cocktail import parsers

class TestParser(unittest.TestCase):

  def setUp(self):
    self.ingredient_parser = parsers.IngredientParser()

  def test_ingredient_parser(self):
    ingredients = self.ingredient_parser.parse_from_file('resources/ingredients.txt')
    
    self.assertEqual(91, len(ingredients))
    self.assertEqual('acaciahonung', ingredients[0])
    self.assertEqual('äppeljuice', ingredients[90])