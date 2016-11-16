#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'thorsen'

from flask import Flask, jsonify, request, send_file
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

import db
import utilities
import config


app = Flask(__name__, static_url_path='', static_folder='../static')
app.config.from_pyfile('config.py')

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
@crossdomain(origin='*')
def root():
    return send_file('../templates/index.html')


@app.route('/recipe/<recipe>')
@crossdomain(origin='*')
def search_recipe(recipe=None):
    recipe = db.recipe_by_name(recipe)
    ingredients = _ingredients_dict_from_list(db.recipe_item_by_recipe(recipe))

    return jsonify(result=(dict(
        name=recipe.name,
        id=recipe.recipe_id,
        description=recipe.description,
        ingredients=ingredients,
        display_src=recipe.display_src
    )))


def _ingredients_dict_from_list(ingredients_list):
    ingredients = {}
    for ingredient in ingredients_list:
        if ingredient.amount:
            ingredients[ingredient.name] = ingredient.amount
        else:
            ingredients[ingredient.name] = None
    return ingredients


@app.route('/ingredients/<ingredient>')
@crossdomain(origin='*')
def search_ingredient(ingredient=None):
    result = []

    was_type, _ = utilities.is_type(ingredient)
    if was_type:
        for ingredient in db.ingredients_by_type(ingredient):
            _append_to_result_list(ingredient, result, was_type=True)
    else:
        was_substring_of_type, types = utilities.is_substring_of_type(ingredient)
        if was_substring_of_type:
            for match in types:
                entry = db.ingredients_by_type(match)[0]
                _append_to_result_list(entry, result, was_type=True)
        for ingredient in db.ingredients_by_name(ingredient):
            _append_to_result_list(ingredient, result)

    return jsonify(result=result)


def _append_to_result_list(ingredient, result, was_type=False):
    if ingredient:
        result.append(dict(
            name=ingredient.name,
            name2=ingredient.name2,
            type=ingredient.type,
            categorySearch=was_type))


@app.route('/recipesbyingredients', methods=['GET'])
def search_recipes_by_ingredient():
    recipes = {}
    result = []
    ingredients = [ingredient.lower() for ingredient in request.args.get('key', '').split(',')]

    type_ingredients, name_ingredients = utilities.split_on_types(ingredients)

    # search by type
    for type in db.distinct_types(type_ingredients):
        for recipe_item in db.recipe_items_by_ingredient_type(type):
            for recipe in db.recipe_by_recipe_item(recipe_item):
                add_ingredient(recipes, recipe, recipe_item)

    # search by name
    for ingredient in name_ingredients:
        for ingredient_item in db.ingredients_by_exact_names(ingredient):
            for recipe_item in db.recipe_items_by_ingredient_name(ingredient_item):
                for recipe in db.recipe_by_recipe_item(recipe_item):
                    add_ingredient(recipes, recipe, recipe_item)

    for recipe in recipes:
        num_of_ingredients = recipes[recipe]['numberOfIngredients']
        num_of_matches = len(recipes[recipe]['matches'])

        difference = num_of_ingredients - num_of_matches

        recipes[recipe]['nonMatches'] = list(recipes[recipe]['nonMatches'] - recipes[recipe]['matches'])
        recipes[recipe]['matches'] = list(recipes[recipe]['matches'])
        recipes[recipe]['difference'] = difference

    sorted_recipes = sorted(recipes.items(), key=lambda x: (x[1]['difference'], x[1]['numberOfIngredients']))
    result.append(dict(recipes=sorted_recipes))

    return jsonify(result=result)


def add_ingredient(recipes_dict, recipe, recipe_item):
    """Adds an ingredient to a recipe if not already present"""
    if recipe.name not in recipes_dict:
        recipes_dict[recipe.name] = {}
        ingredients = set()
        ingredients.add(recipe_item.name)

        all_ingredients = set(item.name for item in db.recipe_item_by_recipe(recipe))

        recipes_dict[recipe.name]['numberOfIngredients'] = len(all_ingredients)
        recipes_dict[recipe.name]['matches'] = ingredients
        recipes_dict[recipe.name]['nonMatches'] = all_ingredients
    else:
        recipes_dict[recipe.name]['matches'].add(recipe_item.name)

if __name__ == "__main__":
    app.run(port=config.PORT, host=config.HOST, debug=config.DEBUG)
