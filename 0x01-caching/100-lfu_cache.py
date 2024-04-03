#!/usr/bin/env python3
"""
LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ class that implements the least frequency used algo for caching """

    def __init__(self):
        """ init method to initailize parent's init """
        super().__init__()
        self.least = []
        self.freq = {}

    def put(self, key, item):
        """assign to self.cache_data the item value for the key """
        if key is None or item is None:
            return
        length = len(self.cache_data)

        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            l = min(self.freq.values())
            l_k = []
            for key, value in self.freq.items():
                if value == l:
                    l_k.append(key)
            if len(l_k) > 1:
                l_f = {}
                for key in l_k:
                    l_f[key] = self.least.index(key)
                discard_k = min(l_f.values())
                discard_k = self.least[discard_k]
            else:
                discard_k = l_k[0]

            print(f"DISCARD: {discard_k}")
            del self.cache_data[discard_k]
            del self.least[self.least.index(discard_k)]
            del self.freq[discard_k]
        if key in self.freq:
            self.freq[key] += 1
        else:
            self.freq[key] = 1
        if key in self.least:
            del self.least[self.least.index(key)]
        self.least.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key is None and key not in self.cache_data:
            return None
        if key in self.least:
            del self.least[self.least.index(key)]
        self.least.append(key)
        if key in self.freq:
            self.freq[key] += 1
        else:
            self.freq[key] = 1
        return self.cache_data.get(key)               
