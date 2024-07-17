#!/usr/bin/env python3

"""
This module provides functions for retrieving
web pages and caching the results.
"""

import requests
import time
from functools import wraps
from typing import Dict


def cached(expiration_time: int):
    """
    Decorator to cache the result of a function with an expiration time.

    Args:
        expiration_time: The time in seconds until the cache expires.

    Returns:
        The decorated function.
    """
    def decorator(func):
        cache = {}

        @wraps(func)
        def wrapper(url):
            if url in cache and \
                    time.time() - cache[url]['timestamp'] < expiration_time:
                cache[url]['count'] += 1
                return cache[url]['content']

            content = func(url)
            cache[url] = {
                'content': content,
                'timestamp': time.time(),
                'count': 1
            }
            return content

        return wrapper

    return decorator


@cached(expiration_time=10)
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a web page.

    Args:
        url: The URL of the web page.

    Returns:
        The HTML content of the web page as a string.
    """
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    # Example usage
    url = ('http://slowwly.robertomurray.co.uk/delay/1000/url/'
           'http://www.google.co.uk')
    for _ in range(5):
        print(get_page(url))
        time.sleep(2)
