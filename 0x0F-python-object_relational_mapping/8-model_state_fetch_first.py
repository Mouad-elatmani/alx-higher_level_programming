#!/usr/bin/python3
"""Link"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def execute_cmd(username, password, dbname):
    db_URL = f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    engine = create_engine(db_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(State.id).first()
    if row is None:
        print("Nothing")
    else:
        print(f"{row.id}: {row.name}")


if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    execute_cmd(username, password, dbname)
