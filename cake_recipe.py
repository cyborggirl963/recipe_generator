from ingredient import Ingredient
from collections import defaultdict
from random import randint

class Cake_Recipe:
    def __init__(self,name):
        self.name = name
        self.ingredients = []
    
    def add_ingredient(self,ingredient_instructions):
        self.ingredients.append(ingredient_instructions)
    
    def print_ingredients(self):
        ingredient_string = ''
        for i in range(0,len(self.ingredients)):
            item = self.ingredients[i]
            for j in range(0,len(item)):
                ingredient_string = ingredient_string + item[j] + ' '
            ingredient_string = ingredient_string + '\n'
        return(ingredient_string)

def unit_ml(unit,quantity):
    unit_dict = {'tablespoon':15,'teaspoon':5,'cup':250,'egg':50}
    ml = unit_dict.get(unit)
    vol = ml*quantity
    return vol

def cake_sublists(ingredient_list):
    ingredient_sublists = defaultdict(list)
    for i in range(0,len(ingredient_list)):
        if Ingredient.is_cake(ingredient_list[i]):
            list_type = Ingredient.return_type(ingredient_list[i])
            ingredient_sublists[list_type].append(ingredient_list[i])
    
    return ingredient_sublists

def special_cake(sublists):
    specials = randint(1,3)
    special_list = []
    special_ingr = []
    if specials==1:
        special_list.extend(sublists['Vegetable'])
    elif specials==2:
        special_list.extend(sublists['Condiments'])
    elif specials==3:
        special_list.extend(sublists['Vegetable'])
        special_list.extend(sublists['Condiments'])

    for i in range(0,randint(1,2)):
        item = special_list.pop(randint(0,len(special_list)-1))
        special_ingr.append(item)
        
    return special_ingr

def water_ratio(cake_ingredients):
    wet = 0
    dry = 0
    for ingr in cake_ingredients:
        water = Ingredient.return_water(ingr)
        unit = Ingredient.return_unit(ingr)
        quant = Ingredient.return_quantity(ingr)
        ml = unit_ml(unit,quant)
        if water=='wet':
            wet = wet + ml
        if water=='dry':
            dry = dry + ml
        if water=='medium':
            wet = wet + ml/2
            dry = dry + ml/2
    
    ratio = wet - dry
    return ratio

def to_instructions(ingredient):
    unit = Ingredient.return_unit(ingredient)
    name = Ingredient.return_name(ingredient)
    quantity = Ingredient.return_quantity(ingredient)
    instructions = [str(quantity),unit,name]
    return instructions

def cake_generator(ingredient_list):
    sublists = cake_sublists(ingredient_list)
    name = ''
    spec_cake = randint(0,1)
    cake_ingr = []
    
    cake_ingr.append(sublists['Oil'].pop(randint(0,len(sublists['Oil'])-1)))
    cake_ingr.append(sublists['Sugar'].pop(randint(0,len(sublists['Sugar'])-1)))
    cake_ingr.append(sublists['Eggs'].pop())

    if spec_cake==1:
        specs = special_cake(sublists)
        cake_ingr.extend(specs)
        for i in range(0,len(specs)):
            name = name + Ingredient.return_name(specs[i]) + ' '
       
    for i in range(0,randint(1,2)):
        cake_ingr.append(sublists['Flour'].pop(randint(0,len(sublists['Flour'])-1)))
    for i in range(0,randint(1,3)):
        spice = sublists['Spices'].pop(randint(0,len(sublists['Spices'])-1))
        cake_ingr.append(spice)
        if spec_cake==0:
            name = name + Ingredient.return_name(spice) + ' '
    
    cake_ingr.append(sublists['Leavening'].pop())
    
    for ingr in cake_ingr:
        Ingredient.gen_quantity(ingr)
    
    rat = water_ratio(cake_ingr)
    print(rat)
    if rat>0:
        flour = sublists['Flour'].pop()
        Ingredient.update_quantity(flour,0.5)
        cake_ingr.append(flour)
    if rat<-200:
        liquid = sublists['Base'].pop()
        Ingredient.update_quantity(liquid,0.5)
        cake_ingr.append(liquid)
    
    name = name + 'Cake'
    
    recipe = Cake_Recipe(name)
    for i in range(0,len(cake_ingr)):
        ingr = to_instructions(cake_ingr[i])
        #print(ingr)
        Cake_Recipe.add_ingredient(recipe,ingr)
    
    return recipe
    
