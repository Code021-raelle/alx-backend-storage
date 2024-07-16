#!/usr/bin/env python3
"""
10-update_topics.py
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a collection's document
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
