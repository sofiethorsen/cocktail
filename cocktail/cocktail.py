#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'thorsen'

from collections import defaultdict
import json

import db

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

if __name__ == "__main__":
  app.run(port=5000, host='0.0.0.0', debug=True)
