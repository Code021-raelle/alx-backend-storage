#!/usr/bin/env python3
"""
Insert a new document into a collection based on keyword arguments
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
