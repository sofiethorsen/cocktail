#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from cocktail import parsers

class TestIngredientParser(unittest.TestCase):

  def setUp(self):
    self.parser = parsers.IngredientParser()

  def test_parse_one(self):
    ingredients = self.parser.parse_from_file('tests/testfiles/ingredient1.txt')

    self.assertEqual(1, len(ingredients))
    self.assertEqual('acaciahonung', ingredients[0])

  def test_parse_ten(self):
    ingredients = self.parser.parse_from_file('tests/testfiles/ingredient10.txt')

    self.assertEqual(10, len(ingredients))
    self.assertEqual('blåbär', ingredients[9])

class TestRecipeParser(unittest.TestCase):

  def setUp(self):
    self.parser = parsers.RecipeParser()

  def test_parse_one(self):
    recipes = self.parser.parse_from_file('tests/testfiles/recipe1.txt')

    self.assertEqual(1, len(recipes))

  def test_parse_ten(self):
    recipes = self.parser.parse_from_file('tests/testfiles/recipe10.txt')

    self.assertEqual(10, len(recipes))

  def test_parse_name(self):
    recipes = self.parser.parse_from_file('tests/testfiles/recipe1.txt')

    self.assertEqual('A Manda Shot', recipes[0].name)

  def test_parse_number_of_ingredients(self):
    recipes = self.parser.parse_from_file('tests/testfiles/recipe1.txt')

    self.assertEqual(4, len(recipes[0].ingredients))

  def test_parse_description(self):
    recipes = self.parser.parse_from_file('tests/testfiles/recipe1.txt')
    desc = ('Fyll ett shotglas med mandarinvodka. Doppa apelsinklyftan i grenadin '
    'och därefter i socker. Balansera apelsinklyftan elegant ovanpå glaset och servera.')

    self.assertEqual(desc, recipes[0].description)




