#!/usr/bin/python
# -*- coding: utf-8 -*-

DB_URI = 'postgresql://drinkappuser@localhost/drinkapp'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model import Article, Ingredient, Recipe, RecipeItem

engine = create_engine(DB_URI, encoding='utf-8')
Session = sessionmaker(bind=engine)
session = Session()


for recipe in session.query(Recipe).all():
	ingredients = set()
	for recipe_item in session.query(RecipeItem).filter_by(recipe_id=recipe._id).all():
		name = recipe_item.name
		for article in session.query(Article).filter(
			Article.name.ilike('%' + name + '%') | 
			Article.name2.ilike('%' + name + '%') |
			Article.category.ilike('%' + name + '%')).all():
			if article.name not in ingredients:
				ingredients.add(article.name)
				ingredient = Ingredient(article.name, article.name2, article.category)
				session.add(ingredient)

session.commit()