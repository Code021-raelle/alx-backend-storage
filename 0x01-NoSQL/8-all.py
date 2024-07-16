#!/usr/bin/env python3
"""
8-all.py
"""


def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection
    """
    documents = list(mongo_collection.find())
    return documents
