#!/usr/bin/env python3
""" Provides stats about Nginx logs restored in mongoDB"""
import pymongo as pm
db = pm.MongoClient()
mydb = db["logs"]
mycol = mydb["nginx"]


if __name__ == "__main__":
    get_get = mycol.count_documents({"method": "GET"})
    get_post = mycol.count_documents({"method": "POST"})
    get_put = mycol.count_documents({"method": "PUT"})
    get_patch = mycol.count_documents({"method": "PATCH"})
    get_delete = mycol.count_documents({"method": "DELETE"})
    get_total = mycol.count_documents({})
    get_status = mycol.count_documents({"method": "GET", "path": "/status"})

    print("{} logs".format(get_total))
    print("Methods:\n\tmethod GET: {}\n\tmethod POST: {}\n\tmethod PUT: {}\n\tmethod PATCH: {}\n\tmethod DELETE: {}".format(
        get_get, get_post, get_put, get_patch, get_delete))
    print("{} status check".format(get_status))
