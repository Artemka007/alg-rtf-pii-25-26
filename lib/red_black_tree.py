import sys
from typing import Literal, Optional, TypeVar

TKey = TypeVar('TKey')

class Node[TKey]:
    def __init__(
        self, 
        key: TKey, 
        color: Literal['red', 'black'],
        parent: Optional['Node[TKey]'] = None, 
        left: Optional['Node[TKey]'] = None, 
        right: Optional['Node[TKey]'] = None, 
    ):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.key}, {self.color})"

class RedBlackTree[TKey]:
    def __init__(self):
        self.nil = Node(None, 'black')
        self.root: Node[TKey] = self.nil

    def insert(self, key: TKey):
        node = Node(key, 'red', left=self.nil, right=self.nil)
        
        parent = self.nil
        current = self.root
        
        while current != self.nil:
            parent = current
            if node.key < current.key:
                current = current.left
            elif node.key > current.key:
                current = current.right
            else:
                return
        
        node.parent = parent
        
        if parent == self.nil:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        self._fix_insert(node)

    def _fix_insert(self, node: Node[TKey]):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._left_rotate(node.parent.parent)
            
            if node == self.root:
                break
        
        self.root.color = 'black'

    def _left_rotate(self, x: Node[TKey]):
        y = x.right
        x.right = y.left
        
        if y.left != self.nil:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    def _right_rotate(self, y: Node[TKey]):
        x = y.left
        y.left = x.right
        
        if x.right != self.nil:
            x.right.parent = y
        
        x.parent = y.parent
        
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y
        y.parent = x

    def search(self, key: TKey) -> bool:
        return self._search(self.root, key)

    def _search(self, node: Node[TKey], key: TKey) -> bool:
        while node != self.nil:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def print_tree(self, node: Optional[Node[TKey]] = None, level: int = 0, prefix: str = "Root:"):
        if node is None:
            node = self.root
        if node != self.nil:
            print(" " * (level * 4) + prefix + f" {node.key}({node.color})")
            if node.left != self.nil:
                self.print_tree(node.left, level + 1, "L---")
            if node.right != self.nil:
                self.print_tree(node.right, level + 1, "R---")