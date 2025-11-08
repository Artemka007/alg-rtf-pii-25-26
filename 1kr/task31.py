from typing import Literal
from lib.set import Set
from lib.quick_sort import quick_sort


class Query:
    def __init__(self, parity: bool, position: tuple[int, int]):
        self.parity = parity
        self.position = position
        
class Solution:
    def __init__(self, N: int, Q: int, queries: list[Query], positions: Set[int]):
        self.N = N
        self.Q = Q

        self.queries = queries
        self.compress_coordinates(positions)

    def solve(self):
        answer = self.Q

        for i, q in enumerate(self.queries):
            x = self.position_to_id[q.position[0]]
            y = self.position_to_id[q.position[1]]
            if not self.union(x, y, q.parity):
                answer = i - 1
                break
            
        return str(answer)

    def find(self, x: int):
        if self.parent[x] != x:
            root, pr = self.find(self.parent[x])
            self.rel_parity[x] = (self.rel_parity[x] + pr) % 2
            self.parent[x] = root
        
        return self.parent[x], self.rel_parity[x]

    def union(self, x: int, y: int, parity_xy: int):
        rx, px = self.find(x)
        ry, py = self.find(y)

        if rx == ry:
            return (px ^ py) == parity_xy
        
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
            x, y = y, x
            px, py = py, px
            
        new_par = px ^ py ^ parity_xy
        self.parent[ry] = rx
        self.rel_parity[ry] = new_par
        self.rank[rx] += self.rank[rx] == self.rank[ry]

        return True
    
    def compress_coordinates(self, positions: Set[int]):
        sorted_positions = list(positions)
        quick_sort(sorted_positions)

        self.position_to_id = {p: i for i, p in enumerate(sorted_positions)}
        self.parent = list(range(len(sorted_positions)))
        self.rank = [0] * len(sorted_positions)
        self.rel_parity = [0] * len(sorted_positions)
        


while True:
    N = int(input())
    if N == -1:
        break
    Q = int(input())

    positions = Set[int]()
    queries: list[Query] = []
    for _ in range(Q):
        q = input().split()
        answer = q[0]
        l = int(q[1])
        r = int(q[2])

        positions.add(l - 1)
        positions.add(r)
        queries.append(Query(answer == 'odd', (l, r)))

    s = Solution(N, Q, queries, positions)
    print(s.solve())