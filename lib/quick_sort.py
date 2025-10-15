import sys
from types import NoneType
from typing import Callable, List, TypeVar

T = TypeVar('T')


sys.setrecursionlimit(100000)

def partiotion[T](items: List[T], low_bound: int, up_bound: int, key: Callable[[T], bool]=lambda x: x):
    pivot = items[up_bound]

    i = low_bound - 1

    for j in range(low_bound, up_bound):
        if not (key(items[j]) < key(pivot)):
            continue
        i += 1
        items[j], items[i] = items[i], items[j]
    
    items[i + 1], items[up_bound] = items[up_bound], items[i + 1]
    return i + 1


def quick_sort[T](
    items: List[T], 
    low_bound: int | NoneType = None, 
    up_bound: int | NoneType = None, 
    key: Callable[[T], bool]=lambda x: x
) -> List[T]:
    if low_bound is None:
        low_bound = 0
        
    if up_bound is None:
        up_bound = len(items) - 1
    
    if low_bound >= up_bound:
        return
    
    pivot_index = partiotion(items, low_bound, up_bound, key=key)

    quick_sort(items, low_bound, pivot_index-1, key=key)
    quick_sort(items, pivot_index+1, up_bound, key=key)


def custom_partiotion[T](items: List[T], comp_func: Callable[[T, T], bool], low_bound: int, up_bound: int):
    pivot = items[up_bound]

    i = low_bound - 1

    for j in range(low_bound, up_bound):
        if not comp_func(items[j], pivot):
            continue
        i += 1
        items[i], items[j] = items[j], items[i]
    
    items[i + 1], items[up_bound] = items[up_bound], items[i + 1]
    return i + 1


def custom_quick_sort[T](items: List[T], comp_func: Callable[[T], bool], low_bound: int, up_bound: int):
    if low_bound > up_bound:
        return
    
    pivot_index = custom_partiotion(items, comp_func, low_bound, up_bound)

    custom_quick_sort(items, comp_func, low_bound, pivot_index - 1)
    custom_quick_sort(items, comp_func, pivot_index + 1, up_bound)