#!/usr/bin/env python3
""" Base Cache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """method to assign to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """method to retreive from the dictionary"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
