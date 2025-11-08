import sys
from lib.quick_sort import quick_sort
from test_func import universal_test_solution

def solution(n1, n2, numbers):
    array1 = []
    array2 = []
    result, i, j, k = 0, 0, 0, 0

    for i in range(n1):
        array1.append(numbers[i])

    for i in range(n1, n2 + n1):
        array2.append(numbers[i])
    
    quick_sort(array1)
    quick_sort(array2)
    
    while j < len(array1) and k < len(array2):
        if array1[j] == array2[k]:
            result += 1
            k += 1
            j += 1
            continue
        
        if array1[j] > array2[k]:
            k += 1
            continue
        
        if array1[j] < array2[k]:
            j += 1
            continue
    
    return result

# ТЕСТОВЫЕ КЕЙСЫ
test_cases = [
    # Базовые тесты
    {
        'input': {
            'n1': 3,
            'n2': 4,
            'numbers': [1, 3, 5, 2, 4, 6, 7, 8]
        },
        'expected': 0  # array1: [1,3,5], array2: [2,4,6,7] - общие: нет
    },
    {
        'input': {
            'n1': 3,
            'n2': 4, 
            'numbers': [1, 3, 5, 3, 4, 6, 7, 8]
        },
        'expected': 1  # array1: [1,3,5], array2: [3,4,6,7] - общие: 3,4
    },
    {
        'input': {
            'n1': 2,
            'n2': 3,
            'numbers': [1, 2, 3, 4, 5]
        },
        'expected': 0  # array1: [1,2], array2: [3,4,5] - общие: нет
    },
    
    # Граничные случаи - пустые массивы
    {
        'input': {
            'n1': 0,
            'n2': 0,
            'numbers': []
        },
        'expected': 0
    },
    {
        'input': {
            'n1': 3,
            'n2': 0,
            'numbers': [1, 2, 3]
        },
        'expected': 0
    },
    {
        'input': {
            'n1': 0,
            'n2': 3, 
            'numbers': [4, 5, 6]
        },
        'expected': 0
    },
    
    # Граничные случаи - один элемент
    {
        'input': {
            'n1': 1,
            'n2': 1,
            'numbers': [5, 5]
        },
        'expected': 1
    },
    {
        'input': {
            'n1': 1,
            'n2': 1,
            'numbers': [5, 6]
        },
        'expected': 0
    },
    
    # Все элементы общие
    {
        'input': {
            'n1': 3,
            'n2': 3,
            'numbers': [1, 2, 3, 1, 2, 3]
        },
        'expected': 3
    },
    
    # Нет общих элементов
    {
        'input': {
            'n1': 2,
            'n2': 2,
            'numbers': [1, 2, 3, 4]
        },
        'expected': 0
    },
    
    # Большие числа
    {
        'input': {
            'n1': 2,
            'n2': 2,
            'numbers': [1000000, 2000000, 3000000, 4000000]
        },
        'expected': 0
    },
    {
        'input': {
            'n1': 3,
            'n2': 2,
            'numbers': [10, 20, 30, 20, 30]
        },
        'expected': 2
    },
    
    # Отрицательные числа
    {
        'input': {
            'n1': 3,
            'n2': 3,
            'numbers': [-1, -2, -3, -2, -3, -4]
        },
        'expected': 2
    },
    
    # Повторяющиеся элементы в одном массиве
    {
        'input': {
            'n1': 4,
            'n2': 3,
            'numbers': [1, 1, 2, 2, 1, 2, 3]
        },
        'expected': 2  # array1: [1,1,2,2], array2: [1,2,3] - общие: 1,2
    },
    
    # Частичное пересечение
    {
        'input': {
            'n1': 4,
            'n2': 5,
            'numbers': [1, 3, 5, 7, 2, 3, 6, 7, 8]
        },
        'expected': 2  # array1: [1,3,5,7], array2: [2,3,6,7,8] - общие: 3,7
    }
]

# ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ
performance_tests = [
    {
        'input': {
            'n1': 1000,
            'n2': 1000,
            'numbers': list(range(1000)) + list(range(500, 1500))
        },
        'expected': 500
    },
    {
        'input': {
            'n1': 1000,
            'n2': 1000,
            'numbers': [1] * 1000 + [2] * 1000
        },
        'expected': 0
    },
    {
        'input': {
            'n1': 1000,
            'n2': 1000, 
            'numbers': list(range(1000)) + list(range(1000))
        },
        'expected': 1000
    }
]

if __name__ == "__main__":
    # Вызов функции тестирования
    print("ОСНОВНЫЕ ТЕСТЫ")
    universal_test_solution(solution, test_cases)
    
    print("\n\n" + "="*100)
    print("ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ")
    universal_test_solution(
        solution, 
        performance_tests,
        show_input_preview=3,
        show_output_preview=1
    )