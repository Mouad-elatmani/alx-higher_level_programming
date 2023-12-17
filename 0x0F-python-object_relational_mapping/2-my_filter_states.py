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
    temp = f"SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(search)
    cur.execute(temp)
    rows = cur.fetchall()
    for i in rows:
        print(i)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
