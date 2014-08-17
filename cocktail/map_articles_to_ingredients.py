#!/usr/bin/python
# -*- coding: utf-8 -*-

import db

import utilities
from model import Ingredient

for recipe in db.all_recipes():
    found_articles = set()
    for recipe_item in db.recipe_items_by_recipe_id(recipe):

        was_type, alcohol_type = utilities.is_type(recipe_item.name.lower())
        if was_type:
            for article in db.articles_by_type(alcohol_type):
                if article not in found_articles:
                    found_articles.add(article)
                    ingredient = Ingredient(article.name, article.name2, article.type)
                    db.add(ingredient)
        else:
            for article in db.article_by_name_or_type(recipe_item.name):
                if article not in found_articles:
                    found_articles.add(article)
                    ingredient = Ingredient(article.name, article.name2, article.type)
                    db.add(ingredient)

db.commit()