from random import randint

class Ingredient:
    def __init__(self,name,tag_list):
        self.name = name
        self.tags = {}
        self.quantity = 0
        for i in range(0,len(tag_list)):
            cat,tag = tag_list[i].split(':')
            self.tags[cat] = tag
    
    def gen_quantity(self):
        ingr_range = {'Oil':(4,8,1),'Flour':(1,3,2),'Sugar':(1,3,2),'Spices':(1,3,1),'Vegetable':(1,2,2),'Condiments':(1,4,1),'Eggs':(1,3,1),'Base':(1,1,1)}
        kind = Ingredient.return_type(self)
        range = ingr_range.get(kind)
        min = range[0]
        max = range[1]
        div = range[2]
        self.quantity = randint(min,max)/div
        return self.quantity

    def update_quantity(self,quant):
        self.quantity = quant

    def return_quantity(self):
        return self.quantity
    
    def return_name(self):
        return self.name
    
    def add_tag(self,tag_key,tag_value):
        self.tags[tag_key] = tag_value
    
    def return_type(self):
        return self.tags['Type']
    
    def return_unit(self):
        return self.tags['Unit']
    
    def is_cake(self):
        cat = self.tags['Category']
        if 'cake' in cat:
            return True
        else:
            return False
    
    def is_stew(self):
        cat = self.tags['Category']
        if 'stew' in cat:
            return True
        else:
            return False
    
    def return_water(self):
        return self.tags['Water']
    
    def return_tags(self):
        return self.tags

