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
            lowest_keys = [
                k for k, v in self.usage_count.items() if v == lowest_value
            ]  # nopep8
            lowest_usage = min(self.usage[k] for k in lowest_keys)
            key_to_remove = min(
                k for k in lowest_keys if self.usage[k] == lowest_usage
            )  # nopep8

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
