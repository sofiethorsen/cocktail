#!/usr/bin/python
# -*- coding: utf-8 -*-

from parsers import IngredientParser, RecipeParser
from model import Ingredient, Recipe, RecipeItem

import db

ingredients = IngredientParser().parse_from_file('../resources/ingredients.txt')
recipes = RecipeParser().parse_from_file('../resources/recipes.txt')

# add all ingredients to db
for ingredient in ingredients:
  Ingredient(ingredient, None, ingredient)
  db.add_model(Ingredient(ingredient, None, ingredient))

# add all recipes and the recipe items mapped to thems
for recipe in recipes:
  recipe_entry = Recipe(recipe.name, recipe.description)
  db.add_model(recipe_entry)

  for substance, amount, metric in recipe.ingredients:
    substance = unicode(substance.decode('utf-8'))
    if not amount:
      recipe_item = RecipeItem(recipe_entry._id, substance, None)
    else:
      tail = unicode((amount + ' ' + metric).decode('utf-8'))
      recipe_item = RecipeItem(recipe_entry._id, substance, tail)
    db.add_model(recipe_item)