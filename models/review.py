#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review object."""

    place_id = ""
    user_id = ""
    text = ""
