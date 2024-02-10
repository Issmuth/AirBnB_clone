#!/usr/bin/python3
"""Defines the city class module."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a City object."""

    state = ""
    name = ""
