from typing import List


def binary_search(array: List[int], n: int, left: int, right: int):
    if array[0] == n:
        return array[0]
    
    while left < right:
        mid = (left + right) // 2 + 1
        s = (right - left + 1) // 2

        if array[mid] == n:
            return mid

        if array[mid] > array[0] and n > array[mid]\
          or n > array[mid] and n < array[0] \
            or array[0] < array[mid] and n < array[0]:
            left += s
            continue

        if array[mid] < array[0] and n < array[mid]\
          or n < array[mid] and n > array[0]\
           or array[0] > array[mid] and n > array[0]:
            right -= s
            continue

    return 1

def solution(n: int, k: int, *items: int):
    return binary_search(list(items), k, 0, n - 1)

test = [i for i in range(10**3, 10**6 + 1)] + [i for i in range(0, 10**3)]
for i in range(10**3, 10**6 + 1, 1000):
    print(i, solution(len(test), i, *test) == i - 1000)
    
    