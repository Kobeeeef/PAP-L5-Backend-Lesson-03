# Practice Session
# Exercise 1
# Import sqlite3
# Import display from visualizer.py
# Connect to the simplefolks database and get a cursor

import sqlite3
from visualizer import display

conn = sqlite3.connect('simplefolks.sqlite')
cursor = conn.cursor()

# Exercise 2
# Create a new table named party 
# Give it 5 columns and assign the appropriate data type:
# Election year
# Name
# Headquarters
# Members
# Fundraising YTD
# make sure to check the table does not exist
# Run a SELECT query and show the output with the visualizer 
# to check that everything worked
# Run this file in terminal

cursor.execute('''
    CREATE TABLE IF NOT EXISTS party (
        Election_Year INTEGER,
        Name TEXT,
        Headquarters TEXT,
        Members INTEGER,
        Fundraising_YTD REAL
    )
''')

cursor.execute('SELECT * FROM party')
display(cursor)

# Exercise 3
# Create an INSERT query to the party table to add 4
# politcal parties and their data 
# Add a value to all columns
# You can look up real information or make up fantasy political parties
# Run a SELECT all query with rowid
# Show the output with the visualizer to check that everything worked
# Run this file in terminal

cursor.execute('''
    INSERT INTO party VALUES 
     (2024, 'Democratic Party', 'Washington, DC', 150000, 2500000.00),
    (2024, 'Republican Party', 'Washington, DC', 80000, 1500000.50),
    (2024, 'Libertarian Party', 'Washington, DC', 120000, 3200000.75),
    (2024, 'Green Party', 'Chicago, IL', 95000, 2100000.00)
''')

cursor.execute('SELECT rowid, * FROM party')
display(cursor)

# Exercise 4
# Create an INSERT query to the party table to add 1 new poltical party that has no money
# Make sure to select the columns that will receive values
# Run a SELECT all query
# Show the output with the visualizer to check that everything worked
# Run this file in terminal

cursor.execute('''
    INSERT INTO party (Election_Year, Name, Headquarters, Members)
    VALUES (2025, 'Bridge Troll Party', 'Seattle, WA', 57)
''')
cursor.execute('SELECT * FROM party')
display(cursor)

# Exercise 5 Create a SELECT all query to the politicians table in the simplefolks.sqlite database so you can see
# what's in it Call the display function to show results on tables.html Create an INSERT  query to add 2 new
# politicians For these 2 politicians set state, party, first_name, last_name, and birth_year, as no other data is
# avialable for them. Make up fictitious politicians if you want, Joe Smith, etc. Execute the insert query Run
# another SELECT query to check if the INSERT query worked Call the display function to show results on tables.html
# Run this file in terminal

cursor.execute('SELECT * FROM politicians')
display(cursor)

cursor.execute('''
    INSERT INTO politicians (state, party, first_name, last_name, birth_year) VALUES 
    ('Washington', 'Dream Party', 'Joe', 'Smith', 1975), 
    ('California', 'Green Future', 'Emily', 'Johnson', 1980)
''')
cursor.execute('SELECT * FROM politicians')
display(cursor)
