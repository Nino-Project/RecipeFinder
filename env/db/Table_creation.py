# To create tables under ingredients.db


import sqlite3

# Connect to the db
con = sqlite3.connect('ingredients.db')

# Creating a cursor
cur = con.cursor()

# Creating a table

# full_ingredients table will serve as a collection of
#   known ingredients in the world.
cur.execute("""CREATE TABLE full_ingredients (
    food_name DATATYPE TEXT,
    food_group DATATYPE TEXT,
    food_subgroup DATATYPE TEXT
    )""")

# user_ingredients table will collect user's available ingredients.
cur.execute("""CREATE TABLE user_ingredients (
    food_name DATATYPE TEXT
    )""")

# Commit
con.commit()

# Closing connection
con.close()
