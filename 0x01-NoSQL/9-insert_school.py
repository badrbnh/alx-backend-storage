#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs"""
    query = mongo_collection.insert_one(kwargs)
    return query.inserted_id
