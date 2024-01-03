#!/usr/bin/env python3
"""
Class the Inherits from BaseCaching
for fifo caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    LifoCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initilize LifoCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        Using fifo logic
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            return self.cache_data.get(key)
