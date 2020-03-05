# TODO
import csv
from cs50 import SQL
from sys import argv, exit

# load sql db file
db = SQL("sqlite:///students.db")
# checking for command-line arguments
if len(argv) != 2:
    print('Missing command-line arguments!')
    exit(1)

# open csv file from user argument
with open(argv[1], 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['name'].split()
        # insert null as a middle name
        if len(name) == 2:
            name.insert(1, None)
        house = row['house']
        birth = row['birth']

        db.execute("INSERT INTO students(first,middle,last,house,birth) VALUES(?,?,?,?,?)",
                   [name[0], name[1], name[2], house, birth])