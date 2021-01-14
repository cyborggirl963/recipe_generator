import csv_parser as parse
from ingredient import Ingredient
import cake_recipe as c

file_name = input()

pantry = parse.parse(file_name)
cake = c.cake_generator(pantry)
print(c.Cake_Recipe.print_ingredients(cake))