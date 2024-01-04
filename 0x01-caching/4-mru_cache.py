#!/usr/bin/python3
"""MRUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A Most Recently Used (MRU) caching system"""

    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache using MRU strategy"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                removed_key = self.stack.pop()
                self.cache_data.pop(removed_key)
                print(f'DISCARD: {removed_key}')
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with the given key"""
        if key in self.cache_data:
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
