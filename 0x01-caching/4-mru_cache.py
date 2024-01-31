#!/usr/bin/env python3
""" LRUCache module """
from base_caching import BaseCaching
from datetime import datetime


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

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            max_key = max(self.usage, key=self.usage.get)
            del self.cache_data[max_key]
            del self.usage[max_key]
            print(f"DISCARD: {max_key}")

        self.usage[key] = datetime.now()
        self.cache_data[key] = item

    def get(self, key):
        """method to retreive from the dictionary"""
        if key is None or self.cache_data.get(key) is None:
            return None

        self.usage[key] = datetime.now()
        return self.cache_data[key]
