#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache class inherits from BaseCaching and is a caching system using LFU algorithm
    """

    def __init__(self):
        """
        Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            items_to_discard = [k for k, v in self.frequency.items() if v == min_freq]
            if len(items_to_discard) > 1:
                # If there are multiple items with the least frequency,
                # we use LRU algorithm to determine which item to discard
                lru_item = min(items_to_discard, key=lambda x: self.cache_data[x][1])
                del self.cache_data[lru_item]
                del self.frequency[lru_item]
                print("DISCARD:", lru_item)
            else:
                discard_key = items_to_discard[0]
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                print("DISCARD:", discard_key)

        self.cache_data[key] = (item, 0)
        self.frequency[key] = 0

    def get(self, key):
        """
        Get an item by key
        """
        if key is None:
            return None

        if key in self.cache_data:
            self.frequency[key] += 1
            self.cache_data[key] = (self.cache_data[key][0], self.frequency[key])
            return self.cache_data[key][0]

        return None

if __name__ == "__main__":
    my_cache = LFUCache()
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
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
