from typing import Tuple, TypeVar

from lib import custom_quick_sort


T = TypeVar('T')
    

def comp_func(item: Tuple[str, int, int], pivot: Tuple[str, int, int]):
    if item[1] > pivot[1]:
        return True
    
    if item[1] == pivot[1] and item[2] < pivot[2]:
        return True
    
    if item[1] == pivot[1] and item[2] == pivot[2] and item[0].lower() < pivot[0].lower():
        return True
    
    return False


def solution(n: int, *items: Tuple[str, int, int]):
    arr = list(items)
    custom_quick_sort(arr, comp_func, 0, n - 1)

    return arr

print(
    [
        i[0] for i in solution(5, ('alla', 4, 100), ('genna', 6, 1000), ('gosha', 2, 90), ('rita', 2, 90), ('Timofey', 4, 80))
    ]
)

print(
    [
        i[0] for i in solution(5, ('alla', 0, 0), ('genna', 0, 0), ('gosha', 0, 0), ('rita', 0, 0), ('Timofey', 0, 0))
    ]
)