import test_func

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


tests = [
    [0, 1, 4, 9, 0],
    [0, 7, 9, 4, 8, 20],
    [0, 1, 4, 9, 0, 0, 7, 9, 4, 8, 20, 0, 67, 25],
    [0, 0, 0, 0, 4],
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [0, 1, 2, 3, 0, 5, 6, 7, 8],
    [0, 1, 4, 9, 0, 0, 7, 9, 4, 8]*10**5,
    [0, 1, 4, 9, 0, 0, 7, 9, 4, 10**9]*10**5,
]
test_func.test_func(solution, tests)