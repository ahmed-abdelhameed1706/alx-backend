#!/usr/bin/env python3
""" MRUCache module """
from base_caching import BaseCaching
from collections import defaultdict


class MRUCache(BaseCaching):
    """fifo caching system"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.usage = defaultdict(int)

    def put(self, key, item):
        """method to assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            max_key = max(self.usage, key=self.usage.get)
            del self.cache_data[max_key]
            del self.usage[max_key]
            print(f"DISCARD: {max_key}")

        self.cache_data[key] = item
        self.usage[key] += 1

    def get(self, key):
        """method to retreive from the dictionary"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.usage:
            self.usage[key] += 1
        return self.cache_data[key]