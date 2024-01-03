#!/usr/bin/python3
"""LIFOCache class that inherits from BaseCaching"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """A Last-In-First-Out (LIFO) caching system"""

    def __init__(self):
        """Initialize LIFOCache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache using LIFO strategy"""
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
        return self.cache_data.get(key)
