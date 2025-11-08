from typing import Optional, TypeVar


T = TypeVar('T')


class MaxHeap:
    def __init__(self, initial_items: list[T] = []):
        self.heap_list = []
        self.current_size = 0

        for i in initial_items:
            self.insert(i)
    
    def shift_up(self, i: int):
        while i > 0:
            parent_index = (i - 1) // 2
            if self.heap_list[i] <= self.heap_list[parent_index]:
                break
            self.swap(i, parent_index)
            i = parent_index
    
    def shift_down(self, i: int):
        while 2 * i + 1 < self.current_size: 
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            max_child = left_child
            
            if (right_child < self.current_size and 
                self.heap_list[right_child] > self.heap_list[left_child]):
                max_child = right_child
            
            if self.heap_list[i] >= self.heap_list[max_child]:
                break
            
            self.swap(i, max_child)
            i = max_child

    def max_child(self, i: int) -> int:
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        
        if right_child >= self.current_size:
            return left_child
        
        if self.heap_list[left_child] > self.heap_list[right_child]:
            return left_child
        else:
            return right_child
    
    def insert(self, node: T):
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
    
    def swap(self, i: int, j: int):
        self.heap_list[i], self.heap_list[j] = self.heap_list[j], self.heap_list[i]
    
    def __len__(self) -> int:
        return self.current_size
    
    def empty(self) -> bool:
        return self.current_size == 0