#!/usr/bin/env python3
"""BaseCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basicache class that inherits from basecaching """
    def __init__(self):
        """init function initializes class from parent init method """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assigns to the dictioanry self.cache_data the item value
           for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ returns value in self.cache_data linked to key """
        if key is None or key not in self.cache_data.keys():
            return None
        value = self.cache_data.get(key)

        return value
