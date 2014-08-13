#!/usr/bin/python
# -*- coding: utf-8 -*-

import db

from model import Ingredient

for recipe in db.all_recipes():
    ingredients = set()
    for recipe_item in db.recipe_items_by_recipe_id(recipe):

        name = recipe_item.name
        for article in db.article_by_name_or_type(name):
            if article.name not in ingredients:
                ingredients.add(article.name)
                ingredient = Ingredient(article.name, article.name2, article.type)
                db.add(ingredient)

db.commit()