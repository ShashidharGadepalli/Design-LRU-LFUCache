from evictionpolicy import Evictionpolicy
from Dlinked import Dlinked
class LFUPolicy(Evictionpolicy):

    def __init__(self):
        self.freq = {}
        self.freq_map = {}
        self.min_freq = 0

    def on_access(self, node):
        old_freq = self.freq[node]
        self.freq_map[old_freq].remove(node)

        if self.freq_map[old_freq].isEmpty() and old_freq==self.min_freq:
            self.min_freq+=1
        new_freq = old_freq+1
        self.freq[node]=new_freq

        if new_freq not in self.freq_map:
            self.freq_map[new_freq]=Dlinked()
        self.freq_map[new_freq].insert(node)

    def on_insert(self,node):
        self.freq[node]=1
        if 1 not in self.freq_map:
            self.freq_map[1]= Dlinked()
        self.freq_map[1].insert(node)
        self.min_freq = 1

    def evict(self):
        eviction_tray = self.freq_map[self.min_freq]
        lru = eviction_tray.left.next
        eviction_tray.remove(lru)
        del self.freq[lru]
        return lru