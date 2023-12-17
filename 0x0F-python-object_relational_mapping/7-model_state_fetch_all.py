#!/usr/bin/python3
"""fetch alll"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, text)


def execute_cmd(username, password, dbname):
    db = f'mysql://{username}:{password}@localhost:3306/{dbname}'
    eng = create_engine(db)
    sql_cmd = text("select * from states;")
    with eng.connect() as connection:
        result = connection.execute(sql_cmd)
        for i in result:
            print(f"{i[0]}: {i[1]}")


if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    execute_query(username, password, dbname)
