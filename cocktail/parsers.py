class IngredientParser(object):
  def __init__(self):
    pass

  def parse_from_file(self, path):
    with open(path) as ingredients_file:
      return [ingredient.strip('\n') for ingredient in ingredients_file]
