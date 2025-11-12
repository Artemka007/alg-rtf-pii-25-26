from lib import quick_sort
from lib.red_black_tree import RedBlackTree
from test_func import universal_test_solution


def order_independent_hash(numbers: list[int]) -> int:
    hash_value = 0
    MOD = 10**18 + 3
    
    for num in numbers:
        element_hash = hash(str(num)) % MOD
        hash_value = (hash_value + element_hash) % MOD
    
    return hash_value


def solution(N: int, M: int, K: int, items: list[str]):
    rb_tree = RedBlackTree[tuple[int, ...]]()
    
    for i in range(N):
        rb_tree.insert(order_independent_hash([int(j) for j in items[i].split()]))
    
    results = []
    for i in range(N, N + K):
        if rb_tree.search(order_independent_hash([int(j) for j in items[i].split()])):
            results.append("1")
        else:
            results.append("0")
    
    return results