
from typing import List
from lib.quick_sort import quick_sort
from test_func import universal_test_solution
import io
import sys

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

    # Вместо вывода возвращаем операции
    return operations

# Обертка для тестирования с форматом вывода
def solution_wrapper(N: int, M: int, matrix_str: str):
    """Обертка для тестирования с входными данными в виде строки"""
    # Парсим матрицу из строки
    lines = matrix_str.strip().split('\n')
    matrix = []
    for line in lines:
        row = list(map(int, line.split()))
        matrix.append(row)
    
    operations = solution(N, M, matrix)
    
    # Форматируем вывод согласно формату
    output = io.StringIO()
    output.write(f"{len(operations)}\n")
    for op in operations:
        output.write(f"{op[0]} {op[1]} {op[2]}")
    
    return output.getvalue().strip()

# ТЕСТОВЫЕ КЕЙСЫ
test_cases = [
    # Простой тест - уже отсортированная матрица
    {
        'input': {
            'N': 2,
            'M': 2,
            'matrix_str': '1 2\n3 4'
        },
        'expected': '0'  # Нет операций
    },
    {
        'input': {
            'N': 3,
            'M': 3,
            'matrix_str': '1 2 3\n4 5 6\n7 8 9'
        },
        'expected': '0'
    },
    
    # Тест с переставленными строками
    {
        'input': {
            'N': 2,
            'M': 2,
            'matrix_str': '3 4\n1 2'
        },
        'expected': '1\nR 1 2'
    },
    {
        'input': {
            'N': 3,
            'M': 2,
            'matrix_str': '5 6\n1 2\n3 4'
        },
        'expected': '2\nR 1 2\nR 2 3'
    },
    
    # Тест с переставленными колонками
    {
        'input': {
            'N': 2,
            'M': 3,
            'matrix_str': '2 1 3\n5 4 6'
        },
        'expected': '1\nC 1 2'
    },
    {
        'input': {
            'N': 2,
            'M': 4,
            'matrix_str': '3 2 1 4\n7 6 5 8'
        },
        'expected': '2\nC 1 3\nC 2 3'
    },
    
    # Смешанный тест - строки и колонки переставлены
    {
        'input': {
            'N': 2,
            'M': 2,
            'matrix_str': '4 3\n2 1'
        },
        'expected': '3\nR 1 2\nC 1 2\nR 1 2'
    },
    {
        'input': {
            'N': 3,
            'M': 3,
            'matrix_str': '9 8 7\n6 5 4\n3 2 1'
        },
        'expected': '4\nR 1 3\nC 1 3\nC 2 3\nR 1 3'
    },
    
    # Граничные случаи
    {
        'input': {
            'N': 1,
            'M': 1,
            'matrix_str': '1'
        },
        'expected': '0'
    },
    {
        'input': {
            'N': 1,
            'M': 3,
            'matrix_str': '3 1 2'
        },
        'expected': '2\nC 1 2\nC 2 3'
    },
    {
        'input': {
            'N': 3,
            'M': 1,
            'matrix_str': '3\n1\n2'
        },
        'expected': '2\nR 1 2\nR 2 3'
    },
    
    # Тест с повторяющимися элементами
    {
        'input': {
            'N': 2,
            'M': 2,
            'matrix_str': '1 1\n2 2'
        },
        'expected': '1\nR 1 2'
    },
    {
        'input': {
            'N': 2,
            'M': 3,
            'matrix_str': '2 2 1\n1 1 2'
        },
        'expected': '2\nR 1 2\nC 1 3'
    },
    {
        'input': {
            'N': 250,
            'M': 250,
            'matrix_str': '\n'.join([' '.join(map(str, range(250, 0, -1)))] * 250)
        },
        'expected': None  # Проверяем только что не падает
    },
    {
        'input': {
            'N': 100,
            'M': 100,
            'matrix_str': '\n'.join([' '.join(map(str, range(1, 101)))] * 100)
        },
        'expected': '0'
    }
]


if __name__ == "__main__":
    print("ОСНОВНЫЕ ТЕСТЫ СОРТИРОВКИ МАТРИЦЫ")
    print("=" * 100)
    
    # Тестируем основную функцию
    universal_test_solution(
        solution_wrapper,
        test_cases,
        show_input_preview=2,
        show_output_preview=3
    )
    