import parsers, db
from model import Ingredient, Recipe, RecipeItem
from utilities import encode

recipe_parser = parsers.RecipeParser()
ingredient_parser = parsers.IngredientParser()

recipes = recipe_parser.parse_from_file('../resources/recipes.txt')
ingredients = ingredient_parser.parse_from_file('../resources/ingredients.txt')

count = 0
for recipe in recipes:
	count+= 1
	recipe_entry = Recipe(recipe.name, recipe.description)
	db.add_model(recipe_entry)

	for substance, amount, metric in recipe.ingredients:
		amount_descriptor = None
		if amount:
			amount_descriptor = (amount + ' ' + metric)
		
		is_type = True
		if db.articles_by_exact_name(substance):
			is_type = False

		db.add_model(RecipeItem(recipe_entry._id, substance, amount_descriptor, is_type))

print 'Added ' + str(count) + ' recipes'

count = 0
for ingredient in ingredients:
	count +=1
	db.add_model(Ingredient(ingredient, None, ingredient))

print 'Added ' + str(count) + ' ingredients'