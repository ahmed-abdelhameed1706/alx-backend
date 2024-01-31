#!/usr/bin/env python3
""" LRUCache module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """fifo caching system"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.usage = {}

    def put(self, key, item):
        """method to assign to the dictionary"""
        if key is None or item is None:
            return

        if key in self.usage:
            self.usage[key] += 1
        else:
            self.usage[key] = 1

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_key = min(self.usage, key=self.usage.get)
            del self.cache_data[min_key]
            del self.usage[min_key]
            print(f"DISCARD: {min_key}")
        self.cache_data[key] = item

    def get(self, key):
        """method to retreive from the dictionary"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.usage[key] += 1
        return self.cache_data[key]
