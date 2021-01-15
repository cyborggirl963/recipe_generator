import csv
from ingredient import Ingredient

def parse(text_file):
    file_list = []
    reader = csv.reader(text_file)
    for row in reader:
        file_list.append(row)

    cols = file_list.pop(0)
    pantry_list = []

    for i in range(0,len(file_list)):
        row = file_list[i]
        name = ''
        tags = []
        for j in range(0,len(row)):
            if cols[j]=='Name':
                name = row[j]
            else:
                tags.append(str(cols[j]+':'+str(row[j])))
        pantry_item = Ingredient(name,tags)
        pantry_list.append(pantry_item)
    return pantry_list

def open_and_parse(file_path):
    with open(file_path, newline='') as text_file:
        return parse(text_file)