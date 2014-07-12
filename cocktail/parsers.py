#!/usr/bin/python
# -*- coding: utf-8 -*-
from utilities import encode
from model import RecipeObject

def isNumber(x):
  try:
    float(x)
    return True
  except ValueError:
    return False

class IngredientParser(object):
  def __init__(self):
    pass

  def parse_from_file(self, path):
    with open(path) as ingredients_file:
      return [encode(ingredient.strip('\n')) for ingredient in ingredients_file]

class RecipeParser(object):
  def __init__(self):
    pass

  def _getline(self, file):
    return file.readline().strip('\n')

  def _description_from_file(self, file):
    description = ''
    while True:
      line = file.readline()
      if '*' in line:
        break
      description += line
    return description

  def _ingredients_from_file(self, file, lines):
    ingredients = []

    for i in range(lines):
      ingredient = self._getline(file)

      if len(ingredient.split(' ')) == 1: 
        ingredients.append((encode(ingredient), '', ''))
      else:
        parts = ingredient.split(' ')

        containsNoDigits = True
        for part in parts:
          if isNumber(part):
            containsNoDigits = False

        if containsNoDigits:
          ingredients.append((encode(ingredient), '', ''))
        else:
          amount, metric, substance = parts[0], parts[1], ' '.join(parts[2:])
          ingredients.append((encode(substance), encode(amount), encode(metric)))

    return ingredients

  def parse_from_file(self, path):
    recipes = []
    with open(path) as recipes_file:
      while(True):
        name = encode(self._getline(recipes_file))
        if not name: break 
        number_of_ingredients = int(recipes_file.readline())   
        ingredients = self._ingredients_from_file(recipes_file, number_of_ingredients)
        description = encode(self._description_from_file(recipes_file))
        recipes.append(RecipeObject(name, description.strip('\n'), ingredients))
    return recipes
