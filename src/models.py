import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(25),  nullable=False)

    def serialize(self):
        return{
        "name":self.name, 
        "username":self.username
        }
    
class Characters(Base): 
    __tablename__="characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    eye_color = Column(String(), nullable=False)
    hair_color = Column(String(250), nullable=False)

    def serialze(self):
        return{
            "name":self.name,
            "username":self.username
        }
    
class Vehicles(Base):
    __tablename__="vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    Passengers = Column(String(250), nullable=False)

    def serialize(self):
        return{
        "name":self.name, 
        "username":self.model
        }

class Planets(Base):
    __tablename__="planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

    
    def serialize(self):
        return{
        "name":self.name, 
        "username":self.mass
        }
    
class Favorites(Base):
    __tablename__="favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"),nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    vehicles_id = Column(Integer, ForeignKey("vehicles.id"), nullable=True)
    planets_id = Column(Integer, ForeignKey("planets.id"), nullable=True)

    user = relationship(User)
    characters = relationship(Characters)
    vehicles = relationship(Vehicles)
    planets = relationship(Planets)

    def serialize(self):
        return{
            "user_id":self.user_id,
            "character_id":self.character_id,
            "vehicle_id":self.vehicle_id,
            "planet_id":self.planet_id
        }
        

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
