from typing import List, Tuple

from lib import custom_quick_sort


def solution(N: int, k: int, priorities: List[int], items: List[Tuple[str, ...]]):
    def comp_func(item: Tuple[str, ...], pivot: Tuple[str, ...]):
        compares = [None] * k
        for i in range(k):
            if item[i + 1] == pivot[i + 1]:
                continue
            compares[priorities[i] - 1] = item[i + 1] > pivot[i + 1]

        for i in compares:
            if i is not None:
                return i
            
        return False
    
    custom_quick_sort(items, comp_func, 0, N - 1)

    return items

print(
    solution(3, 3, [2, 1, 3], [('A', 1, 2, 3), ('B', 3, 2, 1), ('C', 3, 1, 2)])
)