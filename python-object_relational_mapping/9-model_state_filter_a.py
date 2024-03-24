#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a' from the
database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)
    for state in query.all():
        print(f"{state.id}: {state.name}")

    session.close()
