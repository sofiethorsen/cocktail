#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Article, Ingredient, Recipe, RecipeItem

DB_URI = 'postgresql://drinkappuser@localhost/drinkapp'

engine = create_engine(DB_URI, encoding='utf-8')
session = sessionmaker(bind=engine)()

def add_model(model):
  session.add(model)
  session.commit()

def all_recipes():
  return session.query(Recipe).all()