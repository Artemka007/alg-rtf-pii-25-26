from typing import Literal, Optional, TypeVar


TKey = TypeVar('TKey')

class Node[TKey]:
    def __init__(
        self, 
        key: TKey, 
        color: Literal['red', 'black'],
        parent: Optional['Node[TKey]']=None, 
        left: Optional['Node[TKey]']=None, 
        right: Optional['Node[TKey]']=None, 
    ):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return self.key
    
    def __str__(self):
        return self.key


class RedBlackTree[TKey]:
    def __init__(self):
        self.root: Optional[Node[TKey]] = None

    def insert(self, key: TKey):
        node = Node(key, 'red')
        if self.root is None:
            self.root = node
            return
        parent = self.root
        q = None

        while parent is not None:
            q = parent
            if parent.key < node.key:
                parent = parent.right
            else:
                parent = parent.left
        node.parent = q
        if q.key < node.key:
            q.right = node
        else:
            q.left = node
        self.fix_insertion(node)
    
    def fix_insertion(self, node: Node[TKey]):
        if node == self.root:
            node.color = 'black'
            return
        
        parent = node.parent
        grandfather = node.parent.parent
        uncle = grandfather.right if parent == grandfather.left else grandfather.left

        while node.parent.color == 'red':
            if parent == grandfather.left:
                if uncle.color == 'red':
                    parent.color = 'black'
                    uncle.color = 'black'
                    grandfather.color = 'red'
                    node = grandfather
                else:
                    if node == parent.right:
                        node = parent
                        self.left_rotate(node)
                    parent.color = 'black'
                    grandfather.color = 'red'
                    self.right_rotate(grandfather)
            else:
                if uncle.color == 'red':
                    parent.color = 'black'
                    uncle.color = 'black'
                    grandfather.color = 'red'
                    node = grandfather
                else:
                    if node == parent.right:
                        node = node.parent
                        self.right_rotate(node)
                    parent.color = 'black'
                    grandfather.color = 'red'
                    self.left_rotate(grandfather)
        self.root.color = 'black'
    
    def left_rotate(self, node: Node[TKey]): ...
    def right_rotate(self, node: Node[TKey]): ...