from lib.max_heap import MaxHeap


def solution(N, K, items: list[int]):
    left = 1
    right = MaxHeap(items).max_child(0)
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        total = 0

        for length in items:
            total += length // mid
        
        if total >= K:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return ans