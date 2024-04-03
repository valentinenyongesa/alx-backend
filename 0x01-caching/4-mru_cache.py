#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inherits from BaseCaching
    and is a caching system using MRU algorithm
    """

    def __init__(self):
        """
        Initialize MRUCache
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None

        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]

        return None


if __name__ == "__main__":
    my_cache = MRUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
