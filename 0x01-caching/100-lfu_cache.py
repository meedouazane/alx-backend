#!/usr/bin/python3
""" FIFO caching """
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching
LRUCache = __import__('3-lru_cache').LRUCache


class LFUCache(BaseCaching):
    """ caching system """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.count_freq = {}

    def put(self, key, item):
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.count_freq.values())
                least_freq_items = [k for k, v in
                                    self.count_freq.items() if v == min_freq]
                for item_key in least_freq_items:
                    self.cache_data.pop(item_key)
                    del self.count_freq[item_key]
            self.cache_data[key] = item
            self.count_freq[key] = 1
        else:
            self.cache_data[key] = item
            self.count_freq[key] += 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.count_freq[key] = self.count_freq.get(key, 0) + 1
        return self.cache_data.get(key)
