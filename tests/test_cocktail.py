#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from cocktail import parser, utilities, categories


class TestParser(unittest.TestCase):
    def test_parse_one_ingredient(self):
        ingredients = parser.parse_ingredients_from_file('tests/testfiles/ingredient1.txt')

        self.assertEqual(1, len(ingredients))
        self.assertEqual('acaciahonung', ingredients[0])

    def test_parse_ten_ingredients(self):
        ingredients = parser.parse_ingredients_from_file('tests/testfiles/ingredient10.txt')
        expected_name = unicode(u'blåbär')

        self.assertEqual(10, len(ingredients))
        self.assertEqual(expected_name, ingredients[9])

    def test_parse_one_recipe(self):
        recipes = parser.parse_recipes_from_file('tests/testfiles/recipe1.txt')

        self.assertEqual(1, len(recipes))

    def test_parse_ten_recipes(self):
        recipes = parser.parse_recipes_from_file('tests/testfiles/recipe10.txt')

        self.assertEqual(10, len(recipes))

    def test_parse_recipe_name(self):
        recipes = parser.parse_recipes_from_file('tests/testfiles/recipe1.txt')

        self.assertEqual('A Manda Shot', recipes[0].name)

    def test_parse_recipe_ingredients(self):
        recipes = parser.parse_recipes_from_file('tests/testfiles/recipe1.txt')

        self.assertEqual(4, len(recipes[0].ingredients))

    def test_parse_recipe_description(self):
        recipes = parser.parse_recipes_from_file('tests/testfiles/recipe1.txt')
        desc = ('Fyll ett shotglas med mandarinvodka. Doppa apelsinklyftan i grenadin '
                'och därefter i socker. Balansera apelsinklyftan elegant ovanpå glaset och servera.')
        desc = unicode(desc.decode('utf-8'))

        self.assertEqual(desc, recipes[0].description)


class TestUtilities(unittest.TestCase):
    def test_is_type_invalid(self):
        is_type, search_term = utilities.is_type('vodk')

        self.assertEqual((False, 'vodk'), (is_type, search_term))

    def test_is_type_valid(self):
        for alcohol_type in categories.all_types:
            self.assertEqual((True, alcohol_type), utilities.is_type(alcohol_type))





