#!/usr/bin/python
# -*- coding: utf-8 -*-
from utilities import encode
from model import RecipeObject


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def _get_line(file):
    return file.readline().strip('\n')


def _description_from_file(file):
    description = ''
    while True:
        line = file.readline()
        if '*' in line:
            break
        description += line
    return description


def _ingredients_from_file(file, lines):
    ingredients = []

    for i in range(lines):
        ingredient = _get_line(file)

        if len(ingredient.split(' ')) == 1:
            ingredients.append((encode(ingredient), '', ''))
        else:
            parts = ingredient.split(' ')

            contains_no_digits = True
            for part in parts:
                if is_number(part):
                    contains_no_digits = False

            if contains_no_digits:
                ingredients.append((encode(ingredient), '', ''))
            else:
                amount, metric, substance = parts[0], parts[1], ' '.join(parts[2:])
                ingredients.append((encode(substance), encode(amount), encode(metric)))

    return ingredients


def parse_ingredients_from_file(path):
    with open(path) as ingredients_file:
        return [encode(ingredient.strip('\n')) for ingredient in ingredients_file]


def parse_recipes_from_file(path):
    recipes = []
    with open(path) as recipes_file:
        while True:
            name = encode(_get_line(recipes_file))
            if not name:
                break
            number_of_ingredients = int(recipes_file.readline())
            ingredients = _ingredients_from_file(recipes_file, number_of_ingredients)
            description = encode(_description_from_file(recipes_file))
            recipes.append(RecipeObject(name, description.strip('\n'), ingredients))
    return recipes
