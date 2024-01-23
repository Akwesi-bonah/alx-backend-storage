#!/usr/bin/env python3
"""Defines insert_school method"""

def insert_school(mongo_collection, **kwargs):
    """ inser new record"""
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
