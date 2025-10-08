from typing import TypeVar


T= TypeVar('T')


class MinQueue[T]:
    def __init__(self):
        self.min_queue = []
        self.main_queue = []

    def push(self, item: T):
        self.main_queue.append(item)

        while self.min_queue and self.min_queue[-1] > item:
            self.min_queue.pop()
        
        self.min_queue.append(item)
    
    def pop(self):
        value = self.main_queue.pop(0)
        
        if value == self.min_queue[0]:
            self.min_queue.pop(0)
        
        return value
    
    def min(self):
        return self.min_queue[0]
    
    def empty(self):
        return len(self.main_queue) == 0
        

queue = MinQueue()

line = None
N = int(input())

for i in range(N):
    line = input()

    if line.startswith('+'):
        n = int(line[1:].strip())
        queue.push(n)

    if queue.empty():
        print("Очередь пуста")
        continue
    
    if line == '?':
        print(queue.min())

    if line == '-':
        queue.pop()