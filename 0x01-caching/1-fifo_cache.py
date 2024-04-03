#!/usr/bin/python3
"""
FIFOCache module
"""
BaseCaching = __import__('0-basic_cache').BaseCaching



class FIFOCache(BaseCaching):
    """class that implements fifo caching algorithm """

    def __init__(self):
        """ init function, initializes data and super class """
        super().__init__()

    def put(self, key, item):
        """ assigns to dictionary self.cache_data the item for the key value
        """
        if (
            len(self.cache_data) >= BaseCaching.MAX_ITEMS and
	    key not in self.cache_data
            ):
            discard_key = next(iter(self.cache_data))
            print(f"DISCARD: {discard_key}")
        self.cache_data[key] = item

    def get(self, key):
        """ returns value in self.cache_data linked to key """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
