#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class inherits from BaseCaching
    and is a caching system using LIFO algorithm
    """

    def __init__(self):
        """
        Initialize LIFOCache
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = self.key_order.pop()
            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None

        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
