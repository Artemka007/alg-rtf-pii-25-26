from typing import TypeVar


T= TypeVar('T')


class Set[T]:
    def __init__(self, items: list[T] | None = None):
        self._items = items if items else []
        self.index = 0

    def add(self, item: T):
        if self.has(item):
            return
        
        self._items.append(item)

    def remove(self, item: T):
        if not self.has(item):
            return
        
        self._items.append(item)

    def has(self, item: T):
        return item in self._items
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self._items):
            raise StopIteration
        item = self._items[self.index]
        self.index += 1
        return item