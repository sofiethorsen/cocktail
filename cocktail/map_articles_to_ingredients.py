#!/usr/bin/python
# -*- coding: utf-8 -*-

import db

from model import Article, Ingredient, Recipe, RecipeItem

for recipe in db.all_recipes():
	ingredients = set()
	for recipe_item in db.recipe_items_by_recipe_id(recipe):

		# only search by type, reducing search space and bad matching
		if recipe_item.is_type:
			for article in db.articles_by_type(recipe_item.name):
				if article not in ingredients:
					ingredients.add(article)
					ingredient = Ingredient(article.name, article.name2, article.category)

		else:
			for article in db.articles_by_name_or_category(recipe_item.name):
				if article not in ingredients:
					ingredients.add(article)
					ingredient = Ingredient(article.name, article.name2, article.category)
					db.add(ingredient)

db.commit()