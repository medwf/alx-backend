#!/usr/bin/env python3
"""
LFUCache  Module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache define
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_data = {}

    def put(self, key, item):
        """
        put a key value to a cache data

        Args:
            key: the key of item.
            item: the item that should stored in cache data.
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                Key = list(self.cache_data)[0]
                del self.cache_data[Key]
                print(f"DISCARD: {Key}")

    def get(self, key):
        """
        get item using key

        Args:
            key: the key of item

        return: item or None if not exist
        """
        value = self.cache_data.get(key, None)
        if key and value:

            # should not move everyone to end.
            self.cache_data.move_to_end(key)
        return value
