#!/usr/bin/env python3
"""
LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class that implements least recently used algo for caching"""

    def __init__(self):
        """init function to initialize parent init """
        super().__init__()
        self.least = []

    def put(self, key, item):
        """ assigns to self.cache_data the item value for the key key """
        if key is None or item is None:
            return
        length = len(self.cache_data)

        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print(f"DISCARD: {self.least[0]}")
            del self.cache_data[self.least[0]]
            del self.least[0]
        if key in self.least:
            del self.least[self.least.index(key)]

        self.least.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ returns value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        del self.least[self.least.index(key)]
        self.least.append(key)
        return self.cache_data.get(key)
