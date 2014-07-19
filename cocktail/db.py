#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from model import Article, Recipe, RecipeItem

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
    (func.lower(Article.category) == func.lower(type))).all()

def recipe_items_by_recipe_id(recipe):
  return session.query(RecipeItem).filter_by(recipe_id=recipe._id).all()

def articles_by_name_or_type(name):
  return session.query(Article).filter(
    Article.name.ilike('%' + name + '%') | 
    Article.name2.ilike('%' + name + '%') |
    Article.type.ilike('%' + name + '%')).all()