from lib.quick_sort import quick_sort
from test_func import universal_test_solution


def solution(n, items):
    if len(items) == 3:
        return items[0] * items[1] * items[2]
    
    items = [i for i in items]
    
    if len(items) == 3:
        return items[0] * items[1] * items[2]
    
    quick_sort(items)

    mx = None

    for i in range(-3, 3):
        for j in range(i + 1, 3):
            for k in range(j + 1, 3):
                mult = items[i] * items[j] * items[k]
                if i == n + j or j == n + i or j == n + k or k == n + j or k == n + i or i == n + k:
                    continue
                if mx is None or mx < mult:
                    mx = mult

    return mx

test_cases = [
    {
        'input': {
            'n': 10,
            'items': [-1, 2, 3, -4, -2, 5, -1, 5, -3, -2]
        },
        'expected': 75 
    },
    {
        'input': {
            'n': 5,
            'items': [1, 2, 3, 4, 5]
        },
        'expected': 60
    },
    {
        'input': {
            'n': 6,
            'items': [-10, -10, 5, 2, 1, 3]
        },
        'expected': 500
    },
    {
        'input': {
            'n': 4,
            'items': [-1, -2, -3, -4]
        },
        'expected': -6  # -1 * -2 * -3 = -6 (наименее отрицательное)
    },
    
    # Граничные случаи
    {
        'input': {
            'n': 3,
            'items': [1, 2, 3]
        },
        'expected': 6  # 1 * 2 * 3 = 6
    },
    {
        'input': {
            'n': 3, 
            'items': [-1, -2, -3]
        },
        'expected': -6  # -1 * -2 * -3 = -6
    },
    
    # С нулями
    {
        'input': {
            'n': 5,
            'items': [0, 1, 2, 3, 4]
        },
        'expected': 24  # 2 * 3 * 4 = 24
    },
    {
        'input': {
            'n': 4,
            'items': [0, -1, -2, -3]
        },
        'expected': 0  # 0 * -1 * -2 = 0
    },
    {
        'input': {
            'n': 6,
            'items': [0, 0, -1, -2, -3, -4]
        },
        'expected': 0  # после удаления нулей останется 4 числа
    },
    
    # Смешанные случаи
    {
        'input': {
            'n': 7,
            'items': [1, 10, 2, 9, 3, 8, 4]
        },
        'expected': 720  # 8 * 9 * 10 = 720
    },
    {
        'input': {
            'n': 8, 
            'items': [1, -10, 2, -9, 3, -8, 4, -7]
        },
        'expected':  -10 * -9 * 4 
    },
    
    # Все нули
    {
        'input': {
            'n': 5,
            'items': [0, 0, 0, 0, 0]
        },
        'expected': 0  # после удаления нулей массив пуст?
    },
    
    # Два числа (но по условию n >= 3)
    {
        'input': {
            'n': 2,
            'items': [1, 2]
        },
        'expected': 2  # 1 * 2 = 2? Но по логике должно быть 3 числа
    },
    
    # Большие числа
    {
        'input': {
            'n': 6,
            'items': [1000, 1000, 1000, -1000, -1000, -1000]
        },
        'expected': 1000000000  # 1000 * 1000 * 1000 = 1e9
    },
    
    # Особый случай: два больших отрицательных и одно большое положительное
    {
        'input': {
            'n': 5,
            'items': [-100, -90, 1, 2, 3]
        },
        'expected': 27000  # -100 * -90 * 3 = 27000
    },
    {
        'input': {
            'n': 1000,
            'items': list(range(-500, 500))
        },
        'expected': -500 * 499 * -499 
    },
    {
        'input': {
            'n': 1000,
            'items': [i if i % 2 == 0 else -i for i in range(1000)]
        },
        'expected': None  # Проверяем только что не падает
    }
]

if __name__ == "__main__":
    print("ОСНОВНЫЕ ТЕСТЫ ПОИСКА МАКСИМАЛЬНОГО ПРОИЗВЕДЕНИЯ")
    universal_test_solution(
        solution, 
        test_cases,
        show_input_preview=5,
        show_output_preview=1
    )