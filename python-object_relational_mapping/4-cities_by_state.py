import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    database = MySQLdb.connect(host="localhost", port=3306,
                               user=username,
                               passwd=password,
                               db=database)

    cursor = database.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
         FROM cities JOIN states ON states_id = states.id \
         ORDER BY cities.id ASC")

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    database.close()