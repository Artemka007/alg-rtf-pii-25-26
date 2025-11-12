from typing import Optional, TypeVar, List


T = TypeVar('T')


class MinHeap[T]:
    def __init__(self, items: List[T] = None):
        self.heap_list: List[T] = []
        self.current_size = 0

        if items is not None:
            for item in items:
                self.insert(item)
    
    def shift_up(self, i: int) -> None:
        while i > 0:
            parent_index = (i - 1) // 2
            if self.heap_list[i] >= self.heap_list[parent_index]:
                break
            self.swap(i, parent_index)
            i = parent_index
    
    def shift_down(self, i: int) -> None:
        while 2 * i + 1 < self.current_size:
            min_child = self.min_child(i)
            
            if self.heap_list[i] <= self.heap_list[min_child]:
                break
            
            self.swap(i, min_child)
            i = min_child

    def min_child(self, i: int) -> int:
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        if right_child >= self.current_size:
            return left_child
        
        if self.heap_list[left_child] < self.heap_list[right_child]:
            return left_child
        else:
            return right_child
    
    def insert(self, node: T) -> None:
        self.heap_list.append(node)
        self.current_size += 1
        self.shift_up(self.current_size - 1)

    def pop(self) -> Optional[T]:
        if self.current_size == 0:
            return None
        
        root = self.heap_list[0]
        
        self.heap_list[0] = self.heap_list[self.current_size - 1]
        self.heap_list.pop()
        self.current_size -= 1
        
        if self.current_size > 0:
            self.shift_down(0)
        
        return root
    
    def peek(self) -> Optional[T]:
        return self.heap_list[0] if self.current_size > 0 else None
    
    def swap(self, i: int, j: int) -> None:
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
    
    def __len__(self) -> int:
        return self.current_size
    
    def is_empty(self) -> bool:
        return self.current_size == 0
    
    def __str__(self) -> str:
        return f"MinHeap({self.heap_list})"
