from typing import TypeVar


T= TypeVar('T')


class Stack[T]:
    def __init__(self, items: list[T]):
        self.items = items

    def pop(self):
        return self.items.pop()
    
    def push(self, item: T):
        self.items.append(item)