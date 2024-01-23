#!/usr/bin/env python3
"""Defines school_by_topics methods"""

def school_by_topics(mongo_collection, topics):
    """Return list of school having a specific topic"""
    topics_list = {"topics": {"$elemMatch": {"$eq": topics,},},}

    return [doc for doc in mongo_collection.find(topics_list)]