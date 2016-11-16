from sqlalchemy import Column, Integer, Unicode, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = 'articles'

    _id = Column(BigInteger)
    name = Column(Unicode, primary_key=True)
    name2 = Column(Unicode)
    type = Column(Unicode)


class Ingredient(Base):
    __tablename__ = 'ingredients'

    _id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode)
    name2 = Column(Unicode)
    type = Column(Unicode)

    def __init__(self, name, name2, type):
        self.name = name
        self.name2 = name2
        self.type = type


class Recipe(Base):
    __tablename__ = 'recipes'

    _id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode)
    recipe_id = Column(Unicode)
    display_src = Column(Unicode)
    description = Column(Unicode)

    def __init__(self, name, recipe_id, display_src, description):
        self.name = name
        self.recipe_id = recipe_id
        self.description = description
        self.display_src = display_src


class RecipeItem(Base):
    __tablename__ = 'recipe_items'

    _id = Column(Integer, autoincrement=True, primary_key=True)
    recipe_id = Column(Integer)
    name = Column(Unicode)
    amount = Column(Unicode)

    def __init__(self, recipe_id, name, amount):
        self.recipe_id = recipe_id
        self.name = name
        self.amount = amount


class RecipeObject(object):
    def __init__(self, name, recipe_id, display_src, description, ingredients):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.recipe_id = recipe_id
        self.display_src = display_src

    def __str__(self):
        ingredients = ''

        for name, amount, metric in self.ingredients:
            if not amount:
                ingredients += name + '\n'
            else:
                ingredients += '{0} {1} {2}\n'.format(amount, metric, name)

        if ingredients[-2] == ',':
            ingredients = ingredients[:-2]
        else:
            ingredients = ingredients[:-1]

        return self.name + '\nIngredients:\n' + ingredients