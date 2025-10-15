from test_func import universal_test_solution

def solution(n, numbers):
    # создали результирующий массив
    result = [None] * n

    # проходимся слева-направо  
    for i in range(0, n):
        # все нули записываем как ноль
        if numbers[i] == 0:
            result[i] = 0
            continue
        
        if i == 0:
            continue
        
        # если не ноль и значение слева не пустое -- записываем левое значение + 1 
        if result[i - 1] is not None:
            result[i] = result[i - 1] + 1

    # проходимся справо-налево  
    for i in range(n - 1, -1, -1):
        # все нули записываем как ноль
        if numbers[i] == 0:
            result[i] = 0
            continue
        
        if i == n - 1:
            continue
        
        # если не ноль и значение справа не пустое -- записываем правое значение + 1 
        if result[i + 1] is not None and (result[i] is None or result[i + 1] + 1 < result[i]):
            result[i] = result[i + 1] + 1
    
    return result



performance_tests = [
    {
        'input': {'n': 1000000, 'numbers': [0] + [1] * 999999},
        'expected': None  # Проверяем только что не падает
    },
    {
        'input': {'n': 1000000, 'numbers': [1] * 999999 + [0]},
        'expected': None
    },
    {
        'input': {'n': 1000000, 'numbers': [0] * 1000000},
        'expected': [0] * 1000000
    },
    {
        'input': {'n': 1000000, 'numbers': [1] * 1000000},
        'expected': [None] * 1000000
    },
    {
        'input': {'n': 1000000, 'numbers': [0, 1, 4, 9, 0, 0, 1, 4, 9, 0] * 100000},
        'expected': None
    },
]

if __name__ == "__main__":
    print("\n\n" + "="*120)
    print("ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ (большие массивы)")
    print()
    universal_test_solution(
        solution, 
        performance_tests,
        show_input_preview=3,
        show_output_preview=3
    )