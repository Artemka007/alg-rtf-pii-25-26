from typing import Callable, Iterator, List, MutableMapping, Optional, TypeVar


_KT = TypeVar("_KT")  # Key type.
_VT = TypeVar("_VT")  # Value type.


class Element:
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.next: Optional['Element'] = None

        
class Hash(MutableMapping[_KT, _VT]):
    def __init__(self, size: int = 100, hash_func: Callable[[Element], any] | None = None):
        self.size = size
        self.table: List[Element] = [None] * size
        self.count = 0
        self.hash_func = hash_func

    def get(self, key: _KT):
        index = self._hash(key)

        if self.table[index] is None:
            return None

        if self.table[index].key == key:
            return self.table[index]

        current_element = self.table[index]
        while current_element.next is not None:
            current_element = current_element.next
            if current_element.key == key:
                return current_element
            
        return None
    
    def put(self, key: _KT, value: _VT):
        if self.count >= self.size:
            self._rehash()
        
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = Element(key, value)
            self.count += 1
            return

        if self.table[index].key == key:
            self.table[index].value = value
            return

        current_element = self.table[index]
        while current_element.next is not None:
            current_element = current_element.next
        
        current_element.next = Element(key, value)
        self.count += 1

    def remove(self, key: _KT):
        index = self._hash(key)

        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            return True
        
        current_element = self.table[index]
        previous_element = None

        while current_element.next is not None:
            previous_element = current_element
            current_element = current_element.next
            if current_element.key == key:
                previous_element.next = current_element.next
        return True

    def items(self):
        for element in self.table:
            current = element
            while current is not None:
                yield (current.key, current.value)
                current = current.next
    
    def __getitem__(self, key: _KT):
        element = self.get(key)
        if element is None:
            raise KeyError(f"Key '{key}' not found")
        return element.value
    
    def __setitem__(self, key: _KT, value: _VT) -> None:
        self.put(key, value)
    
    def __delitem__(self, key: _KT) -> None:
        if not self.remove(key):
            raise KeyError(f"Key '{key}' not found")
    
    def __contains__(self, key: _KT) -> bool:
        return self.get(key) is not None
    
    def __len__(self) -> int:
        return self.count
    
    def __iter__(self) -> Iterator[_VT]:
        for key, value in self.items():
            yield key
    
    def __str__(self) -> str:
        items = []
        for key, value in self.items():
            items.append(f"'{key}': '{value}'")
        return "{" + ", ".join(items) + "}"
    
    def __repr__(self) -> str:
        return f"Hash(size={self.size}, count={self.count})"

    def _hash(self, key: _KT):
        if self.hash_func:
            return self.hash_func(key)
        if isinstance(key, int):
            return self._hash_int(key)
        if isinstance(key, str):
            return self._hash_str(key)
        return None

    def _hash_str(self, key: str):
        hash_value = 0
        for i, symbol in enumerate(key):
            hash_value = (hash_value * 31 + ord(symbol)) % self.size
        
        return hash_value

    def _hash_int(self, key: int):                
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = (key >> 16) ^ key
        return key % self.size

    def _rehash(self):
        new_table = [None] * (self.size * 2)
        for i in range(len(self.table)):
            new_table[i] = self.table[i]
        
        self.table = new_table
        self.size *= 2
