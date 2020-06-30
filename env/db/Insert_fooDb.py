# Inserting file from FooDB Version 1.0 a csv file
from pathlib import Path
import os
import csv
import sqlite3

current_directory = os.getcwd()
data_folder = Path('Ingredients_Sample_Data/FooDb/')
file_to_open = current_directory / data_folder / "Food.csv"

f = open(file_to_open, 'rt')
read = csv.reader(f)

con = sqlite3.connect('ingredients.db')
cur = con.cursor()

list_append = []

for row in read:
    insert_row = tuple(row)
    list_append.append(insert_row)

cur.executemany(
    "INSERT INTO full_ingredients (food_name, food_group, food_subgroup) VALUES (?, ?, ?)", list_append)

con.commit()
f.close()
con.close()
