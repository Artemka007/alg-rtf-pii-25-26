from typing import Optional, TypeVar


TKey = TypeVar('TKey')

class Node[TKey]:
    def __init__(
        self, 
        key: TKey, 
        parent: Optional['Node[TKey]']=None, 
        left: Optional['Node[TKey]']=None, 
        right: Optional['Node[TKey]']=None, 
    ):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return self.key
    
    def __str__(self):
        return self.key