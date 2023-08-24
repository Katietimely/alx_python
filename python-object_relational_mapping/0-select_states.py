# list of databases
import MySQLdb
import sys


database = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    
# create a cursor to navigate the datebase path 
cursor = database.cursor()
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
database.close()