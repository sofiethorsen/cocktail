import parsers, db
from model import Ingredient, Recipe, RecipeItem
from utilities import encode

recipe_parser = parsers.RecipeParser()
ingredient_parser = parsers.IngredientParser()

recipes = recipe_parser.parse_from_file('../resources/recipes.txt')
ingredients = ingredient_parser.parse_from_file('../resources/ingredients.txt')

for recipe in recipes:
	recipe_entry = Recipe(recipe.name, recipe.description)
	db.add_model(recipe_entry)

	for substance, amount, metric in recipe.ingredients:
		# TODO: fix at parse time instead
		if not isinstance(substance, unicode):
			substance = encode(substance)
		
		if not amount:
			recipe_item = RecipeItem(recipe_entry._id, substance, None)
		else:
			recipe_item = RecipeItem(recipe_entry._id, substance, (amount + ' ' + metric))

		db.add_model(recipe_item)

for ingredient in ingredients:
	db.add_model(Ingredient(ingredient, None, ingredient))