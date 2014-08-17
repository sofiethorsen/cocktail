#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from cocktail import utilities, categories


class TestUtilities(unittest.TestCase):
    def test_is_type_invalid(self):
        is_type, search_term = utilities.is_type('vodk')

        self.assertEqual((False, 'vodk'), (is_type, search_term))

    def test_is_type_valid(self):
        for alcohol_type in categories.all_types:
            self.assertEqual((True, alcohol_type), utilities.is_type(alcohol_type))

    def test_is_substring_of_type_valid(self):
        is_substring, alcohol_types = utilities.is_substring_of_type('rom')

        self.assertEqual((True, {u'rom', u'ljus rom', u'mörk rom'}), (is_substring, set(alcohol_types)))

    def test_is_substring_of_type_invalid(self):
        is_substring, alcohol_types = utilities.is_substring_of_type('x')

        self.assertEqual((False, []), (is_substring, alcohol_types))

    def test_split_on_types(self):
        ingredients = ['vodka', 'havana club', 'rom', 'absolut vodka']

        type_ingredients, name_ingredients = utilities.split_on_types(ingredients)

        self.assertEqual(type_ingredients, {'vodka', 'rom'})
        self.assertEqual(name_ingredients, {'havana club', 'absolut vodka'})
