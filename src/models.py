


import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    def serialize(self):
        return{
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


class Planet(Base):
    __tablename__= 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(150), nullable=True)
    diameter = Column(String(15), nullable=False)
    population = Column(String(18), nullable=False)

    def serialize(self):
        return{
            "id": id.self,
            "name": name.self,
            "url": url.self,
            "diameter": diameter.self,
            "population": population.self
        }


class Character(Base):
    __tablename__= 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url = Column(String(150), nullable=True)
    birth_year = Column(String(15), nullable=False)
    homeworld = Column(String(18), nullable=False)

    def serialize(self):
        return{
            "id": id.self,
            "name": name.self,
            "url": url.self,
            "birth_year": birthyear.self,
            "homeworld": homeworld.self
        }


render_er(Base, 'diagram.png')