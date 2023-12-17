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
    temp = "SELECT name FROM cities where cities.id = (SELECT\
            id from states where name = %s)"
    cur.execute(temp, (search,))
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
