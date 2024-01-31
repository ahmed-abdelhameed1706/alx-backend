#!/usr/bin/env python3
""" fifo caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """method to assign to the dictionary"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                cache_keys = list(self.cache_data.keys())
                self.cache_data.pop(cache_keys[0])
                print(f"DISCARD: {cache_keys[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """method to retreive from the dictionary"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]


my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
