#!/usr/bin/python3
""" FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ caching system """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if BaseCaching.MAX_ITEMS <= len(self.cache_data):
            if key not in self.cache_data:
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print(f'DISCARD: {first_key}')
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
