#!/usr/bin/python3
"""LFUCache class that inherits from BaseCaching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A Least Frequently Used (LFU) caching system"""

    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.queue = []
        self.lfu = {}

    def put(self, key, item):
        """Add an item to the cache using LFU strategy"""
        if key is not None and item is not None:
            if len(self.queue) >= self.MAX_ITEMS and not self.cache_data.get(key):
                discard_key = min(self.lfu, key=lambda k: self.lfu[k])
                self.queue.remove(discard_key)
                self.lfu.pop(discard_key)
                self.cache_data.pop(discard_key)
                print(f'DISCARD: {discard_key}')

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            insert_index = 0
            while (insert_index < len(self.queue)
                   and not self.lfu[self.queue[insert_index]]):
                insert_index += 1
            self.queue.insert(insert_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with the given key"""
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                       self.lfu[key] >= self.lfu[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(
                        self.queue.index(key) + 1,
                        self.queue.pop(
                            self.queue.index(key)))
        return self.cache_data.get(key)
