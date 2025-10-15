from lib.heap import MinHeap


class Solution:
    def __init__(self, n: int, items: list[int]):
        self.n = n
        self.items = items
        self.res = True

    def visit(self, i: int):
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        if not self.res or left_child >= len(self.items) or right_child >= len(self.items):
            return
        
        if self.items[left_child] > self.items[right_child] or self.items[i] > self.items[left_child] or self.items[i] > self.items[right_child]:
            self.res = False
            return
        
        self.visit(left_child)
        self.visit(right_child)
        
    def show_result(self):
        print(self.res)


if __name__ == '__main__':
    heap = MinHeap()
    for i in range(100):
        heap.insert(i)
    heap_l = heap.heap_list.copy()
    s = Solution(len(heap.heap_list), heap.heap_list)
    s.visit(0)
    print(heap.heap_list, s.res)
    s = Solution(len(heap.heap_list[2:29]), heap.heap_list[2:29])
    s.visit(0)
    print(heap.heap_list[2:29], s.res)
    heap_l[0] = heap_l[29]
    s = Solution(len(heap_l), heap_l)
    s.visit(0)
    print(heap_l, s.res)
    s = Solution(5, [1, 1, 1, 1, 1])
    s.visit(0)
    print([1, 1, 1, 1, 1], s.res)

