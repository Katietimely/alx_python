import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    database = MySQLdb.connect(host="localhost", port=3306,
                               user=username,
                               passwd=password,
                               db=database)

    cursor = database.cursor()
    query = "SELECT cities.name FROM cities\
             JOIN states ON cities.state_id = states.id\
             WHERE states.name = %s\
             ORDER BY cities.id ASC"

    cursor.execute(query, (state, ))

    cities = cursor.fetchall()

    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    database.close()