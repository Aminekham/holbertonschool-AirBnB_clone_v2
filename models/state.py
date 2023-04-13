#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """Represent State Model."""

    from models import storage_t

    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ""

        @property
        def cities(self):
            """getting cities related to the state"""
            from models.city import City
            from models import storage
            cities = storage.all(City)
            my_all = []
            for city in cities:
                if cities[city].state_id == self.id:
                    my_all.append(cities[city])
            return(my_all)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)