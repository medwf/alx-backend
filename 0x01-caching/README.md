# Caching Algorithms Project

## Background Context
In this project, you will learn about different caching algorithms and implement them. Caching is a fundamental concept in computing that helps improve efficiency by temporarily storing data that is frequently accessed, thus reducing access time.

## Resources
To complete this project, you should read or watch the following materials:
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First-in_first-out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last-in_first-out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_recently_used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_frequently_used_(LFU))

## Learning Objectives
By the end of this project, you should be able to explain the following concepts to anyone:
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- The purpose of a caching system
- The limitations of a caching system

## Requirements
### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should adhere to the `pycodestyle` style (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your classes should have documentation.
- All your functions (inside and outside a class) should have documentation.
- Documentation should be a real sentence explaining the purpose of the module, class, or method.

### BaseCaching Class
All your classes must inherit from the `BaseCaching` class defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Project Structure
Your project should include the following directories and files:
```
.
├── base_caching.py
├── fifo_cache.py
├── lifo_cache.py
├── lru_cache.py
├── mru_cache.py
├── lfu_cache.py
└── README.md
```

## Implementation Details
1. **FIFO Cache**: Implement a caching system that evicts the first added items first when the cache reaches its limit.
2. **LIFO Cache**: Implement a caching system that evicts the last added items first when the cache reaches its limit.
3. **LRU Cache**: Implement a caching system that evicts the least recently used items first when the cache reaches its limit.
4. **MRU Cache**: Implement a caching system that evicts the most recently used items first when the cache reaches its limit.
5. **LFU Cache**: Implement a caching system that evicts the least frequently used items first when the cache reaches its limit.

Each caching algorithm should be implemented in its respective file and should inherit from `BaseCaching`.

## Usage
To run your caching system, you can create instances of your caching classes and use the `put` and `get` methods to add and retrieve items from the cache. Use the `print_cache` method to display the current state of the cache.

