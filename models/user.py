#!/usr/bin/python3
"""User defining module."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class definition.
    With common user attributes
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
