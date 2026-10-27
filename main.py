from lrucachepolicy import LRUpolicy
from lfucachepolicy import LFUPolicy
from cache import Cache

c = Cache(2,LRUpolicy())
c.put(1,1)
c.put(2,2)
c.put(3,3)
print(c.get(2))
print(c.get(1))

c1 = Cache(3,LRUpolicy())
c1.put(2,2)
c1.put(1,1)
print(c1.get(2))
c1.put(4,4)
print(c1.get(2))
print(c1.get(1))
c1.put(5,5)
c = Cache(2, LRUpolicy())

c.put("user:42", {"name": "Alice", "plan": "pro"})
c.put((3, 4), [1, 2, 3])

print(c.get("user:42"))     # {'name': 'Alice', 'plan': 'pro'}
print(c.get((3, 4)))        # [1, 2, 3]

c.put("user:99", {"name": "Bob", "plan": "free"})   # cache is full, so evicts the least recent

print(c.get("user:42"))     # {'name': 'Alice', 'plan': 'pro'}
print(c.get((3, 4)))        # -1
print(c.get("user:99")) 

####### LFU Cache:
c = Cache(2, LFUPolicy())
c.put(1, 1)
c.put(2, 2)
c.get(1)
c.get(1)             # key 1 used 3 times
c.get(2)             # key 2 used 2 times, and it's the most recent
c.put(3, 3)          # LFU evicts key 2
print(c.get(1))      # 1
print(c.get(2))      # -1
print(c.get(3))  