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
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    capacity = Column(Integer, nullable=False)
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)

    
render_er(Base, 'diagram.png')