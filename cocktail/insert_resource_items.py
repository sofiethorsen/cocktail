import parser
import db
from model import Ingredient, Recipe, RecipeItem

recipes = parser.parse_recipes_from_file('../resources/recipes.txt')
ingredients = parser.parse_ingredients_from_file('../resources/ingredients.txt')

count = 0
for recipe in recipes:
    count += 1
    recipe_entry = Recipe(recipe.name, recipe.description)
    db.add_model(recipe_entry)

    for substance, amount, metric in recipe.ingredients:
        amount_descriptor = None
        if amount:
            amount_descriptor = (amount + ' ' + metric)

        db.add_model(RecipeItem(recipe_entry._id, substance, amount_descriptor))

print 'Added ' + str(count) + ' recipes'

count = 0
for ingredient in ingredients:
    count += 1
    db.add_model(Ingredient(ingredient, None, ingredient))

print 'Added ' + str(count) + ' ingredients'