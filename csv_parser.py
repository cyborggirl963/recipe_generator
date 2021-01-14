import csv
from ingredient import Ingredient

def parse(file_path):
    file_list = []

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
            file_list.append(row)

    cols = file_list.pop(0)
    #print(cols)

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
        #print(name)
        #print(tags)
        pantry_item = Ingredient(name,tags)
        pantry_list.append(pantry_item)
    return pantry_list