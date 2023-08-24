# listing all tables
import MySQLdb
import sys

# connecting a cursor
database = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])


# creating a cursor
cursor = database.cursor()
state_name = sys.argv[4]

cursor.execute(
            "SELECT id, name FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
database.close()