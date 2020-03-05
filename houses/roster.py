import csv
from cs50 import SQL
from sys import argv, exit

# connect sql db to students db
db = SQL("sqlite:///students.db")
# check for user arguments
if len(argv) != 2:
    print('Missing command-line arguments!')
    exit(1)

# create dict to store data
houses = {}

# select all data based on user argument
houses = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last",  argv[1])

for row in houses:
    first = row['first']
    middle = row['middle']
    last = row['last']
    birth = row['birth']
    if row['middle'] == None:
        print(f"{first} {last}, born {birth}")
    else:
        print(f"{first} {middle} {last}, born {birth}")