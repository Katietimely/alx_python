from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class State(Base):
    """
    class of state

    Attributes:
      id(int): the unique identifier for the state
      name(str): the name of the state

    Args:
     Base (DeclarativeMeta): class base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)