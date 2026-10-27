from abc import ABC, abstractmethod

class Evictionpolicy(ABC):

    @abstractmethod
    def on_access(self,node):
        pass

    @abstractmethod
    def on_insert(self,node):
        pass

    @abstractmethod
    def evict(self):
        pass