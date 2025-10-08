class Solution:
    def __init__(self, N: int, K: int):
        self.found_solutions = 0
        self.N = N
        self.K = K
        self.placed_positions = []
        self.occupied_rows = set()
        self.occupied_diagonals_l_to_r = set()
        self.occupied_diagonals_r_to_l = set()

    def backtrack(self, column: int, count: int):
        if count == self.K:
            self.found_solutions += 1
            return
        
        if column == self.N:
            return
        
        self.backtrack(column + 1, count) 

        for row in range(self.N):
            if row in self.occupied_rows or \
                (column + row) in self.occupied_diagonals_l_to_r or \
                (row - column) in self.occupied_diagonals_r_to_l:
                continue
            G_moves = [1 for (c, r) in self.placed_positions if (abs(column - c) == 2 and abs(row - r) == 1) or (abs(column - c) == 1 and abs(row - r) == 2)]
            if len(G_moves) > 0:
                continue
            
            self.occupied_rows.add(row)
            self.occupied_diagonals_l_to_r.add(column + row)
            self.occupied_diagonals_r_to_l.add(row - column )
            self.placed_positions.append((column, row))

            self.backtrack(column + 1, count + 1)

            self.occupied_rows.remove(row)
            self.occupied_diagonals_l_to_r.remove(column + row)
            self.occupied_diagonals_r_to_l.remove(row - column)
            self.placed_positions.pop()
        return self
                
    


print(Solution(10, 3).backtrack(0, 0).found_solutions)