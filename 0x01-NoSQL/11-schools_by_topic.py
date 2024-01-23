#!/usr/bin/env python3
"""Defines school_by_topics methods"""

def school_by_topic(mongo_collection, topic):
    """Return list of school having a specific topic"""
    topics_list = {"topics": {"$elemMatch": {"$eq": topic,},},}
    return [i for i in mongo_collection.find(topics_list)]