#!/usr/bin/python3
"""Imports modules"""
import sys
import MySQLdb


def main():
    usern, pswd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    search = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=usern,
                           passwd=pswd, db=dbname, charset="utf8")
    cur = conn.cursor()
    temp = f"""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = '{search}' ORDER BY cities.id"""
    cur.execute(temp)
    rows = cur.fetchall()
    data = ''
    for i in rows:
        data += ', '.join(i) + ', '
    data = data.rstrip(", ")
    print(data)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
