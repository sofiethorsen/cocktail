#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'thorsen'

from collections import defaultdict
import json

import db
import utilities

from flask import Flask, jsonify, request, send_file
from model import Article, Ingredient, Recipe, RecipeItem

app = Flask(__name__)

@app.route('/articles/<article>')
def search_articles(article=None):
  result = []
  for article in db.article_by_name(article):
    result.append(dict(
      name=article.name, 
      name2=article.name2,
      type=article.type)
    )

  return jsonify(result=result)

@app.route('/recipesbyingredients', methods=['GET'])
def search_recipes_by_ingredient():
  recipes = {}
  result = []
  ingredients = request.args.get('key', '').split(',')

  type_ingredients, name_ingredients = utilities.split_on_types(ingredients)

  # search by type
  for type in db.distinct_types(type_ingredients):
    for recipe_item in db.recipe_items_by_ingredient_type(type):
      for recipe in db.recipe_by_recipe_item(recipe_item):
        add_ingredient(recipes, recipe, recipe_item)


  for recipe in recipes:
    recipes[recipe]['ingredients'] = list(recipes[recipe]['ingredients'])
    recipes[recipe]['numOfMatches'] = len(recipes[recipe]['ingredients'])

  sorted_recipes = sorted(recipes.items(), key = lambda x :x[1]['numOfMatches'], reverse = True)
  result.append(dict(recipes=sorted_recipes))

  return jsonify(result=result)

def add_ingredient(recipes_dict, recipe, recipe_item):
  """Adds an ingredient to a recipe if not already present"""
  if recipe.name not in recipes_dict:
    recipes_dict[recipe.name] = {}
    ingredients = set()
    ingredients.add(recipe_item.name)
    recipes_dict[recipe.name]['ingredients'] = ingredients
  else:
    recipe_item.name 
    recipes_dict[recipe.name]['ingredients'].add(recipe_item.name)

if __name__ == "__main__":
  app.run(port=5000, host='0.0.0.0', debug=True)
