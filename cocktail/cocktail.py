#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'thorsen'

from flask import Flask, jsonify, request, send_file

import db
import utilities


app = Flask(__name__, static_url_path='', static_folder='../static')


@app.route('/')
def root():
    return send_file('../templates/index.html')


@app.route('/recipe/<recipe>')
def search_recipe(recipe=None):
    recipe = db.recipe_by_name(recipe)
    ingredients = _ingredients_dict_from_list(db.recipe_item_by_recipe(recipe))

    return jsonify(result=(dict(
        name=recipe.name,
        description=recipe.description,
        ingredients=ingredients,
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
    app.run(port=5000, host='0.0.0.0', debug=True)
