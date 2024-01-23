#!/usr/bin/env python3
""" Defines update_topics class"""


def update_topics(mongo_collection, name, topics):
    """update all topics of a school based on the name"""
    mongo_collection.update_many(
        {"name": name}, {"$set":{"topics": topics}}
    )