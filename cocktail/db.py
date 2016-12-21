#!/usr/bin/python
# -*- coding: utf-8 -*-

import config

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from model import Article, Recipe, RecipeItem, Ingredient

import categories

engine = create_engine(config.DB_URI, encoding='utf-8')
session = sessionmaker(bind=engine)()


def add(model):
    session.add(model)


def commit():
    session.commit()


def add_model(model):
    session.add(model)
    session.commit()


def all_recipes():
    return session.query(Recipe).all()


def articles_by_exact_name(name):
    return session.query(Article).filter(
        (func.lower(Article.name) == func.lower(name)) |
        (func.lower(Article.name2) == func.lower(name))).all()


def article_by_name(string):
    return session.query(Article).filter(Article.name.ilike('%' + string + '%')).all()


def articles_by_type(type):
    return session.query(Article).filter(
        (func.lower(Article.type) == func.lower(type))).all()


def article_by_name_or_type(string):
    return session.query(Article).filter(
        Article.name.ilike('%' + string + '%') |
        Article.name2.ilike('%' + string + '%') |
        Article.type.ilike('%' + string + '%')).all()


def recipe_by_recipe_item(recipe_item):
    return session.query(Recipe).filter_by(_id=recipe_item.recipe_id).all()

def recipe_by_recipe_id(recipe_id):
    return session.query(Recipe).filter_by(recipe_id=recipe_id).all()


def recipe_items_by_recipe_id(recipe):
    return session.query(RecipeItem).filter_by(recipe_id=recipe._id).all()


def recipe_items_by_ingredient_name(ingredient_item):
    if ingredient_item.name2:
        return session.query(RecipeItem).filter(RecipeItem.name.ilike(ingredient_item.name2)).all()
    else:
        return session.query(RecipeItem).filter(RecipeItem.name.ilike(ingredient_item.name)).all()


def recipe_item_by_recipe(recipe):
    return session.query(RecipeItem).filter_by(recipe_id=recipe._id).all()


def articles_by_name_or_type(name):
    return session.query(Article).filter(
        Article.name.ilike('%' + name + '%') |
        Article.name2.ilike('%' + name + '%') |
        Article.type.ilike('%' + name + '%')).all()


def recipe_by_name(name):
    return session.query(Recipe).filter(
        (func.lower(Recipe.name) == func.lower(name))).first()


def recipe_items_by_ingredient_type(type):
    return session.query(RecipeItem).filter(
        (func.lower(RecipeItem.name) == func.lower(type))).all()


def ingredients_by_name(string):
    return session.query(Ingredient).filter(
        Ingredient.name.ilike(string + '%') |
        Ingredient.name.ilike('% ' + string + '%') |
        Ingredient.name2.ilike(string + '%') |
        Ingredient.name2.ilike('% ' + string + '%')).all()


def ingredients_by_exact_name2(string):
    return session.query(Ingredient).filter(Ingredient.name2.ilike(string)).all()


def ingredients_by_exact_name(string):
    return session.query(Ingredient).filter(Ingredient.name.ilike(string)).all()


def ingredients_by_exact_names(string):
    name2_results = ingredients_by_exact_name2(string)
    if name2_results:
        return name2_results
    else:
        return ingredients_by_exact_name(string)


def ingredients_by_type(string):
    result = []
    matches = [alcohol_type for alcohol_type in categories.all_types if string in alcohol_type]
    for entry in matches:
        search_type = categories.specific_type_mappings[entry]
        result.append(session.query(Ingredient).filter_by(type=search_type).first())
    return result


def distinct_types(input_ingredients):
    result = set()
    alcohol_types = set()

    for ingredient in input_ingredients:
        for alchohol_type, alcohol_type_mapping in categories.specific_type_mappings.items():
            if ingredient.lower() in alchohol_type:
                alcohol_types.add(alcohol_type_mapping)

    for type in alcohol_types:
        descriptions = type.split(', ')
        if len(descriptions) > 1:
            for desc in descriptions:
                result.add(desc)
        else:
            result.add(type)

    return result