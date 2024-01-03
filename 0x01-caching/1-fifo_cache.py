#!/usr/bin/env python3
"""
Class the Inherits from BaseCaching
for fifo caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A First-In-First-Out (FIFO) caching system"""

    def __init__(self):
        """Initialize FIFOCache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache using FIFO strategy"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

            if len(self.queue) > self.MAX_ITEMS:
                removed_key = self.queue.pop(0)
                self.cache_data.pop(removed_key)
                print(f'DISCARD: {removed_key}')

    def get(self, key):
        """Retrieve the value associated with the given key"""
        return self.cache_data.get(key)
