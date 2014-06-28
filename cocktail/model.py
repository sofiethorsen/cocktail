class Recipe(object):
  def __init__(self, name, description, ingredients):
    self.name = name
    self.description = description
    self.ingredients = ingredients

  def __str__(self):
    ingredients = ''

    for name, amount, metric in self.ingredients:
      if not amount:
        ingredients += name + '\n'
      else:
        ingredients +='{0} {1} {2}\n'.format(amount, metric, name) 

    if ingredients[-2] == ',':
      ingredients = ingredients[:-2]
    else:
      ingredients = ingredients[:-1]

    return self.name + '\nIngredients:\n' + ingredients