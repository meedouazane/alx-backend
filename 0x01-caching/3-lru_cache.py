#!/usr/bin/python3
""" FIFO caching """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ caching system """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if BaseCaching.MAX_ITEMS <= len(self.cache_data):
                key_lru, value = self.cache_data.popitem(True)
                print(f'DISCARD: {key_lru}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key)
