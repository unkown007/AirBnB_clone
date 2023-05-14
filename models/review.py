#!/usr/bin/python3
"""Defines Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Implements Review class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
