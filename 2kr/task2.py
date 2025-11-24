import math
from lib.min_heap import MinHeap


def solution(N: int, items: list[int]):
    h = MinHeap(items)
    total = 0

    while len(h) > 1:
        a = h.pop()
        b = h.pop()
        summary = a + b
        total += summary * 0.01
        h.insert(summary * 0.99)
    
    return math.ceil(total * 100) / 100