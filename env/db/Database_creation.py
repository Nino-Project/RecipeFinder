# Purpose of this file is to create a local database


import sqlite3

con = sqlite3.connect('ingredients.db')
con = sqlite3.connect('recipes.db')

# Closing connection
con.close()
