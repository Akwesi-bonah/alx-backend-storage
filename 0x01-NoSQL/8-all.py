#!/usr/bin/python3
""" script that list all document in collection """

def list_all(mongo_collection):
    """ list all document in all collection"""
    if not mongo_collection:
        return []
    
    return [ doc for doc in mongo_collection.find()]