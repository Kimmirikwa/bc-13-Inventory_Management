import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    staff_no = Column(String(10),unique=True, nullable=False)
    staff_role = Column(String(10),nullable=False)


class AssetRecord(Base):
    __tablename__ = 'asset_record'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    asset_name = Column(String(50))
    asset_description = Column(String(250))
    asset_serial_number = Column(String(250), unique=True)
    asset_andela_serial_code = Column(String(250), unique=True)
    asset_date_bought = Column(String(20))
    asset_status = Column(String(20))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)