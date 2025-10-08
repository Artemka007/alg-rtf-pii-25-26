from typing import List, Optional


def binary_search(array: List[int], n: int, left: Optional[int] = None, right: Optional[int] = None):
    if left is None:
        left = 0
    
    if right is None:
        right = len(array) - 1

    
    while left < right:
        mid = (left + right) // 2 + 1
        s = (right - left + 1) // 2

        if n > array[mid]:
            left += s
            continue

        if n < array[mid]:
            right -= s
            continue

        return mid

    return None