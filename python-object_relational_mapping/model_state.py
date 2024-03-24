#!/usr/bin/python3
"""Defines the State model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Column): The state's id.
        name (sqlalchemy.Column): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
