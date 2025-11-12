from lib.hash import Hash


class TrieNode:
    def __init__(self):
        self.children = Hash(26)
        self.is_end = False


class TrieWithHash:
    def __init__(self):
        self.root = TrieNode()
        self.words_set = Hash(1000)
    
    def insert(self, word: str) -> None:
        """Вставляет слово в Trie"""
        node = self.root
        for char in word:
            child_element = node.children.get(char)
            if child_element is None:
                # Создаем новый узел
                new_node = TrieNode()
                node.children.put(char, new_node)
                node = new_node
            else:
                node = child_element.value
        
        node.is_end = True
        self.words_set.put(word, True)
    
    def search(self, word: str) -> bool:
        return self.words_set.get(word) is not None
    
    def can_split(self, word: str) -> bool:
        if len(word) < 2:
            return False
            
        prefix_exists = [False] * (len(word) + 1)
        node = self.root
        
        for i, char in enumerate(word):
            child_element = node.children.get(char)
            if child_element is None:
                break
            node = child_element.value
            prefix_exists[i + 1] = node.is_end
        
        for i in range(1, len(word)):
            if prefix_exists[i] and self.search(word[i:]):
                return True
        
        return False
