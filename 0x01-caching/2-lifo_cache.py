#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class that implements lifo caching algorithm """

    def __init__(self):
        """ init function initializes super to call the parent init """
        super().__init__()
        self.last_mod = []

    def put(self, key, item):
        """assign to the dict self.cache_data the item value for the key key
        """
        if key is None or item is None:
            return
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print(f"DISCARD: {self.last_mod[-1]}")
            del self.cache_data[self.last_mod[-1]]
            del self.last_mod[-1]
            if key in self.last_mod:
                del self.last_mod[self.last_mod.index(key)]
        self.last_mod.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
