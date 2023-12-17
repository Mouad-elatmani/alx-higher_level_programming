#!/usr/bin/python3
"""Imports modules"""
import sys
import MySQLdb


def main():
    usern, pswd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=usern,
                           passwd=pswd, db=dbname, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities INNER\
            JOIN states ON states.id = cities.state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
