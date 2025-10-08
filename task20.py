from typing import List

from lib import quick_sort


def solution(N: int, M: int, matrix: List[List[int]]):
    operations = []

    row_order = list(range(N))
    column_order = list(range(M))

    quick_sort(row_order, key=lambda x: matrix[x][0])
    quick_sort(column_order, key=lambda y: matrix[0][y])


    for i in range(N):
        correct_row = row_order[i]
        if correct_row == i:
            continue

        matrix[i], matrix[correct_row] = matrix[correct_row], matrix[i]
        row_order[i], row_order[correct_row] = row_order[correct_row], row_order[i]
        operations.append(('R', i + 1, correct_row + 1))

    for i in range(M):
        correct_column = column_order[i]

        if correct_column == i:
            continue

        for j in range(N):
            matrix[j][i], matrix[j][correct_column] = matrix[j][correct_column], matrix[j][i]
            
        column_order[i], column_order[correct_column] = column_order[correct_column], column_order[i]
        operations.append(('C', i + 1, correct_column + 1))

    for op in reversed(operations):
        print(f"{op[0]} {op[1]} {op[2]}")


solution(4, 5, [
    [10, 7, 9, 8, 6], 
    [15, 12, 14, 13, 11], 
    [20, 17, 19, 18, 16], 
    [5, 2, 4, 3, 1]
])