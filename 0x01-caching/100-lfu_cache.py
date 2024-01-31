#!/usr/bin/env python3
""" MRUCache module """
from base_caching import BaseCaching
from datetime import datetime
from collections import defaultdict


class LFUCache(BaseCaching):
    """fifo caching system"""

    def __init__(self):
        """init method"""
        super().__init__()
        self.usage_count = defaultdict(int)
        self.usage = {}

    def put(self, key, item):
        """method to assign to the dictionary"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lowest_value = min(self.usage_count.values())
            lowest_keys = [k for k, v in self.usage_count.items() if v == lowest_value]
            lowest_usage = min(self.usage[k] for k in lowest_keys)
            key_to_remove = min(k for k in lowest_keys if self.usage[k] == lowest_usage)

            del self.cache_data[key_to_remove]
            del self.usage[key_to_remove]
            del self.usage_count[key_to_remove]
            print(f"DISCARD: {key_to_remove}")

        self.usage[key] = datetime.now()
        self.usage_count[key] += 1
        self.cache_data[key] = item

    def get(self, key):
        """method to retreive from the dictionary"""
        if key is None or self.cache_data.get(key) is None:
            return None

        self.usage[key] = datetime.now()
        self.usage_count[key] += 1
        return self.cache_data[key]


my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()
