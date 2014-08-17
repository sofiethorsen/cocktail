#!/usr/bin/python
# -*- coding: utf-8 -*-

from cocktail import parser

from model import Ingredient, Recipe, RecipeItem
from utilities import encode

import db

ingredients = parser.parse_ingredients_from_file('../resources/ingredients.txt')
recipes = parser.parse_recipes_from_file('../resources/recipes.txt')


def create_ingredient_from_text(entry):
    return Ingredient(entry, None, entry)


def create_recipe_from_recipe_object(recipe_object):
    return Recipe(recipe_object.name, recipe_object.description)


def create_recipe_item_from_recipe(recipe_object):
    for substance, amount, metric in recipe_object.ingredients:
        substance = encode(substance)

        if not amount:
            return RecipeItem(recipe_object._id, substance, None)
        else:
            return RecipeItem(recipe_object._id, substance, encode(amount + ' ' + metric))


# add all ingredients to db
for ingredient in ingredients:
    db.add_model(create_ingredient_from_text(ingredient))

# add all recipes and the recipe items mapped to them
for recipe in recipes:
    recipe_entry = create_recipe_from_recipe_object(recipe)

    db.add_model(recipe_entry)
    db.add_model(create_recipe_item_from_recipe(recipe_entry))