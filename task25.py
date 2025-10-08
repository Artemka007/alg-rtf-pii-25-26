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


s = Solution(5, [1, 2, 3, 4, 5])
s.visit(0)
s.show_result()

