import random
from lib.max_heap import MaxHeap
from typing import List, Optional

from lib.min_heap import MinHeap

class Element:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next: Optional['Element'] = None

class Hash:
    def __init__(self, size: int = 100):
        self.size = size
        self.table: List[Optional[Element]] = [None] * size
        self.count = 0
    
    def get(self, key: str) -> Optional[int]:
        index = self._hash(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def put(self, key: str, value: int):
        if self.count >= self.size:
            self._rehash()
        
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = Element(key, value)
            self.count += 1
            return
        
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                current.value = value
                return
            prev = current
            current = current.next
        
        prev.next = Element(key, value)
        self.count += 1

    def items(self):
        for element in self.table:
            current = element
            while current is not None:
                yield (current.key, current.value)
                current = current.next
    
    def _hash(self, key: str) -> int:
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def _rehash(self):
        old_table = self.table
        old_size = self.size
        self.size = self.size * 2
        self.table = [None] * self.size
        self.count = 0
        
        for i in range(old_size):
            current = old_table[i]
            while current is not None:
                self.put(current.key, current.value)
                current = current.next

def heap_optimized_solution(N: int, M: int, items: List[str]):
    word_to_docs = Hash(2**16)
    documents = []
    
    for doc_id in range(N):
        document = items[doc_id]
        documents.append(document)
        
        word_freq = Hash(50)
        words = document.split()
        for word in words:
            current = word_freq.get(word) or 0
            word_freq.put(word, current + 1)
        
        for word, freq in word_freq.items():
            docs_map = word_to_docs.get(word)
            if docs_map is None:
                docs_map = Hash(100)
                docs_map.put(str(doc_id), freq)
                word_to_docs.put(word, docs_map)
            else:
                docs_map.put(str(doc_id), freq)
    
    for query_idx in range(N, N + M):
        query = items[query_idx]
        query_words = query.split()
        
        heap = MinHeap()
        doc_scores = Hash(N)
        
        for word in query_words:
            docs_map = word_to_docs.get(word)
            if docs_map is not None:
                for doc_id_str, freq in docs_map.items():
                    doc_id = int(doc_id_str)
                    current = doc_scores.get(str(doc_id)) or 0
                    doc_scores.put(str(doc_id), current + freq)
        
        for doc_id_str, score in doc_scores.items():
            if score > 0:
                heap.insert((score, int(doc_id_str)))
        
        result = []
        for _ in range(min(5, heap.current_size)):
            if heap.is_empty():
                break
            _, doc_id = heap.pop()
            result.append(str(doc_id + 1))
        
        yield result
