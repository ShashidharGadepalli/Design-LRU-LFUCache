from evictionpolicy import Evictionpolicy
from node import Node

class LRUpolicy(Evictionpolicy):

    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def on_access(self,node):
        self._remove(node)
        self._insert(node)

    def on_insert(self, node):
        self._insert(node)

    def evict(self):
        lru = self.left.next
        self._remove(lru)
        return lru

    def _remove(self,node):
        nxt,prv = node.next,node.prev

        nxt.prev = prv
        prv.next = nxt

    def _insert(self,node):

        nxt,prv = self.right,self.right.prev

        nxt.prev = node
        prv.next = node

        node.next = nxt
        node.prev = prv

