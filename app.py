# Exercise 1
# Import sqlite3
# Import the display function from visualizer.py
# Create/Connect to the shop.db database
# Get a cursor so you can write queries to the database

import sqlite3
from visualizer import display

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Exercise 2 
# Create a table called "cart" with 4 columns:
# Item
# Department
# Quantity
# Price
# make sure to check the table does not exist
# Run a SELECT query and show the output with the visualizer 
# to check that everything worked

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        Item TEXT,
        Department TEXT,
        Quantity INTEGER,
        Price REAL
    )
''')

cursor.execute('SELECT * FROM cart')
display(cursor)

# Exercise 3
# Write a INSERT query to add an item to the cart table 
# Make up an item you'd like to buy but perhaps can't afford
# Execute the query
# Create a SELECT query to retrieve the cart table and execute it
# Check the output using the display function

cursor.execute('''
    INSERT INTO cart (Item, Department, Quantity, Price)
    VALUES ('Luxury Watch', 'Accessories', 1, 15000.00)
''')

cursor.execute('SELECT * FROM cart')
display(cursor)

# Exercise 4
# Write a INSERT query to add 3 items to the cart table 
# Imagine items you'd buy on a wild, fantasy shopping trip
# Execute the query
# Create a SELECT query to retrieve the cart table and execute it
# Check the output using the display function

cursor.execute('''
    INSERT INTO cart VALUES 
    ('Private Jet', 'Transport', 1, 50000000.00),
    ('Mansion', 'Real Estate', 1, 10000000.00),
    ('Yacht', 'Leisure', 1, 25000000.00)
''')

cursor.execute('SELECT * FROM cart')
display(cursor)

# Exercise 5
# Write a INSERT query to add an item with no price to the cart table 
# Imagine something priceless that really can't be bought
# Execute the query
# Create a SELECT query to retrieve the cart table and execute it
# Check the output using the display function

cursor.execute('''
    INSERT INTO cart (Item, Department)
    VALUES ('Happiness', 'Emotions')
''')

cursor.execute('SELECT * FROM cart')
display(cursor)
