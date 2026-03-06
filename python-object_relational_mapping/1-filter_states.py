#!/usr/bin/python3
"""Script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ = "__main__":
"""Connect to the DB using command line arguments."""
db = MySQdb.connect(
host="localhost",
port=3306
user=sys.argv[1],
pwd=sys.argv[2],
db=sys.argv[3]
)

cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name = 'N%' ORDER BY states.id ASC;")

states = cur.fetchall()

for state in states:
print(state)

cur.close()
db.close();
