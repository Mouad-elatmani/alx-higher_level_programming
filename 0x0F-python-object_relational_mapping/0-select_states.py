#!/usr/bin/python3
""" Import modules """
import sys
import MySQLdb


def main():
    usern, pswd, dbname, = sys.argv[1], sys.argv[2], sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=usern,
                           passwd=pswd, db=dbname, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
