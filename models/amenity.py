#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, DateTime, Column
# from sqlalchemy.orm import relationship
# from models.place import place_amenity
from os import getenv

class Amenity(BaseModel, Base):
    """class for amenities"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place", secondary=place_amenity,
        #                                viewonly=False)
    else:
        name = ""
