from evictionpolicy import Evictionpolicy
from node import Node

class Cache:

    def __init__(self,capacity,policy:Evictionpolicy):

        if capacity<1:
            raise ValueError("Capacity has to be a postive intger")
        self._capacity = capacity
        self.cache = {}
        self._policy = policy

    def get(self,key):

        if key not in self.cache:
            return -1
        self._policy.on_access(self.cache[key])
        return self.cache[key].val

    def put(self,key,value):

        if key in self.cache:
            self.cache[key].val = value
            self._policy.on_access(self.cache[key])

        else:
            if len(self.cache)>=self._capacity:
                victim = self._policy.evict()
                del self.cache[victim.key]

            self.cache[key]=Node(key,value)
            self._policy.on_insert(self.cache[key])