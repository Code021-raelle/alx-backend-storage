#!/usr/bin/env python3
"""
Module for a simple cache class using redis
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Class for a simple cache using redis
    """

    def __init__(self):
        """
        Initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis and return the key

        Args:
            data (Union[str, bytes, int, float]): The data to store

        Returns:
            str: The key under which the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self,
            key: str,
            fn: Optional[Callable] = None,
            ) -> Union[str, bytes, int, float, None]:
        """
        Get the data from Redis using the given key

        Args:
            key (str): The key under which the data is stored
            fn (Optional[Callable], optional): A function to apply to the data.

        Returns:
            Union[str, bytes, int, float, None]: The data stored under the key
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        """
        Retrive the string data stored in Redis by the given key

        Args:
            key (str): The key under which the data is stored

        Returns:
            Optional[str]: The string data stored under the key
        """
        return self.get(key, lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> Optional[int]:
        """
        Retrive the integer data stored in Redis by the given key

        Args:
            key (str): The key under which the data is stored

        Returns:
            Optional[int]: The integer data stored under the key
        """
        return self.get(key, lambda d: int(d))
    

if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
