#!/usr/bin/python3
"""
A script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()
