#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB,
including the top 10 most present IPs.
"""

from pymongo import MongoClient

def log_stats():
    """
    Displays stats about Nginx logs stored in MongoDB,
    including the top 10 most present IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Total number of documents
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods stats
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: logs_collection.count_documents({"method": method}) for method in methods}
    print("Methods:")
    for method, count in method_stats.items():
        print(f"\tmethod {method}: {count}")

    # Status check
    status_check = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Top 10 IPs
    top_ips = logs_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
