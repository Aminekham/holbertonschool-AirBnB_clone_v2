#!/usr/bin/python3
"""State Module for HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represent State Model."""

    from models import storage_t

    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City')
    else:
        name = ""

        @property.getter
        def cities(self):
            """Citties getter."""
            from models.city import City
            from models import storage
            cities = storage.all(City)
            linked_cities = []
            for city in cities:
                if cities[city].state_id == self.id:
                    linked_cities.append(cities[city])
            return linked_cities

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)