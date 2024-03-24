#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username, password, database, search_name = sys.argv[1:5]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == search_name).first()
    if result:
        print(f"{result.id}")
    else:
        print("Not found")

    session.close()
