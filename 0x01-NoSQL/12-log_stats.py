#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
    Displays stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: logs_collection.count_documents({"method": method}) for method in methods}
    print("Methods:")
    for method, count in method_stats.items():
        print(f"\tmethod {method}: {count}")

    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
