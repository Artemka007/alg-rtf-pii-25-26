from typing import List, Optional, TypeVar


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

class BinaryTree[TKey]:
    def __init__(self):
        self.root: Optional[Node[TKey]] = None
    
    def inorder_traversal(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root
        self.inorder_traversal(self, node.left)
        print(node.key)
        self.inorder_traversal(self, node.right)
    
    def preorder_traversal(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root
        print(node.key)
        self.inorder_traversal(self, node.left)
        self.inorder_traversal(self, node.right)
    
    def postorder_traversal(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root
        self.inorder_traversal(self, node.left)
        self.inorder_traversal(self, node.right)
        print(node.key)

    def search(self, key: TKey):
        node = self.root

        while node:
            if node.key == key:
                break
            
            if node.key < key:
                node = node.right
            
            if node.key > key:
                node = node.left
        
        return node
    
    def min(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root

        while node.left:
            node = node.left
        
        return node
    
    def max(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root

        while node.right:
            node = node.right
        
        return node
    
    def next(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root

        if node.right is not None:
            return self.min(node.right)
        
        q = node.parent

        while q is not None and node == q.right:
            node = q
            q = q.parent
        
        return q
    
    def prev(self, node: Optional['Node[TKey]']=None):
        node = node if node else self.root

        if node.left is not None:
            return self.max(node.left)
        
        q = node.parent

        while q is not None and node == q.left:
            node = q
            q = q.parent
        
        return q
    
    def insert(self, key: TKey):
        node = self.root
        parent = None

        while node:
            if node.key < key and node.right:
                node = node.right
            
            if node.key < key and not node.right:
                new_node = Node(key, node)
                node.right = new_node
                new_node.parent = node
            
            if node.key > key and node.left:
                node = node.left
            
            if node.key > key and not node.left:
                new_node = Node(key, node)
                node.left = new_node
                new_node.parent = node

        return node

    def delete(self, key: TKey):
        return self._delete(self.root, key)
    
    def _delete(self, root: Node[TKey], key: TKey):
        if root is None:
            return None
        
        if key < root.key:
            root.left = self._delete(root.left, key)
        
        if key > root.key:
            root.right = self._delete(root.right, key)
        
        if key == root.key and root.left and root.right:
            root.key = self.min(root.right).key
            root.right = self._delete(root.right, root.key)
        
        if key == root.key and root.left and not root.right:
            root = root.left
        
        if key == root.key and not root.left and root.right:
            root = root.right
        
        return root

    def alternative_delete(self, node: Node[TKey], key: TKey):
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            return

        if node.left is None:
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            return

        if node.right is None:
            if node.parent.right == node:
                node.parent.right = node.right
            else:
                node.parent.left = node.right

            return
        
        next_node = self.next(node.parent)
        next_node.right = node.right
        next_node.left = node.left
        next_node.parent = node.parent

        if node.parent.left == node:
            node.parent.left = next_node
        else:
            node.parent.right = next_node