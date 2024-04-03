#!/usr/bin/env python3
"""
MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ class that implements most recently used algo for caching """

    def __init__(self):
        """ init function to call parent's class init """
        super().__init__()
        self.most = []

    def put(self, key, item):
        """ assign to self.cache_data the item value for the key """
        if key is None or item is None:
            return
        length = len(self.cache_data)

        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print(f"DISCARD: {self.most[-1]}")
            del self.cache_data[self.most[-1]]
            del self.most[-1]
        if key in self.most:
            del self.most[self.most.index(key)]
        self.most.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        if key in self.most:
            del self.most[self.most.index(key)]
        self.most.append(key)
        return self.cache_data.get(key)
