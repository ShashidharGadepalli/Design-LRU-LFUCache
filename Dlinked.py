from node import Node
class Dlinked:

    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        nxt,prv = node.next,node.prev
        nxt.prev = prv
        prv.next = nxt

    def insert(self,node):

        nxt,prv = self.right,self.right.prev

        nxt.prev = node
        prv.next = node

        node.next = nxt
        node.prev = prv

    def isEmpty(self):
        return self.left.next == self.right