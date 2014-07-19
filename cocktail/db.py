#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from model import Article, Recipe, RecipeItem, Ingredient

import categories

DB_URI = 'postgresql://drinkappuser@localhost/drinkapp'

engine = create_engine(DB_URI, encoding='utf-8')
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

def recipe_by_recipe_item(recipe_item):
  return session.query(Recipe).filter_by(_id=recipe_item.recipe_id).all()

def recipe_items_by_recipe_id(recipe):
  return session.query(RecipeItem).filter_by(recipe_id=recipe._id).all()

def articles_by_name_or_type(name):
  return session.query(Article).filter(
    Article.name.ilike('%' + name + '%') | 
    Article.name2.ilike('%' + name + '%') |
    Article.type.ilike('%' + name + '%')).all()

def recipe_items_by_ingredient_type(type):
  return session.query(RecipeItem).filter(
    (func.lower(RecipeItem.name) == func.lower(type))).all()

def distinct_types(input_types):
  result = set()
  types = set()

  for word in input_types:
    for key, values in categories.case_insensitive_categories.items():
      if word.lower() in values:
        types.add(categories.all_categories[key])

  for type in types:
    descriptions = type.split(', ')
    if len(descriptions) > 1:
      for desc in descriptions: 
        result.add(desc)
    else:
        result.add(type)

  return result