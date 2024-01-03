#!/usr/bin/python3
"""LRUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A Least Recently Used (LRU) caching system"""

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache using LRU strategy"""
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
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
