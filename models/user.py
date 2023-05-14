#!/usr/bin/python3
"""This module defines user class"""


from models.base_model import BaseModel


class User(BaseModel):
    """Implements User class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
