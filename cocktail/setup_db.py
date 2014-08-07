#!/usr/bin/python
# -*- coding: utf-8 -*-
from cocktail.parser import parse_ingredients_from_file, parse_recipes_from_file

from model import Ingredient, Recipe, RecipeItem
from utilities import encode

import db

ingredients = parse_ingredients_from_file('../resources/ingredients.txt')
recipes = parse_recipes_from_file('../resources/recipes.txt')

# add all ingredients to db
for ingredient in ingredients:
    Ingredient(ingredient, None, ingredient)
    db.add_model(Ingredient(ingredient, None, ingredient))

# add all recipes and the recipe items mapped to thems
for recipe in recipes:
    recipe_entry = Recipe(recipe.name, recipe.description)
    db.add_model(recipe_entry)

    for substance, amount, metric in recipe.ingredients:
        substance = encode(substance)
        if not amount:
            recipe_item = RecipeItem(recipe_entry._id, substance, None)
        else:
            tail = encode(amount + ' ' + metric)
            recipe_item = RecipeItem(recipe_entry._id, substance, tail)
        db.add_model(recipe_item)