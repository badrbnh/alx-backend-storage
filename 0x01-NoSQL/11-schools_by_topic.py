#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic:"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic:"""
    cursor = mongo_collection.find({'topics': topic}, {'_id': 0, 'name': 1})
    
    # Extract the names of schools from the cursor
    school_names = [document['name'] for document in cursor]
    
    return school_names
